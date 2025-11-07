#!/usr/bin/env python3
"""
Comprehensive Tournament Results Visualization Suite
Creates organized visualizations and text analysis for both creativity and syntax tournaments
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os
import re
from collections import defaultdict

# Set style
plt.style.use('default')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

def parse_results_file(file_path):
    """Parse tournament results file into structured data"""
    results = []
    
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    for line in lines:
        if not line.strip() or 'FINAL ELO RANKINGS' in line:
            continue
            
        match = re.match(r'\s*(\d+)\.\s+(.+?)\s+\(ELO:\s+(\d+),\s+Record:\s+(\d+-\d+),\s+Win Rate:\s+([\d.]+)%,\s+Buchholz:\s+(\d+)\)', line)
        if match:
            rank, filename, elo, record, win_rate, buchholz = match.groups()
            results.append({
                'rank': int(rank),
                'filename': filename,
                'elo': int(elo),
                'record': record,
                'win_rate': float(win_rate),
                'buchholz': int(buchholz)
            })
    
    return results

def extract_strategy_info(filename, task_type):
    """Extract strategy and parameters from filename"""
    name = filename.replace('.txt', '')
    
    if task_type == 'creativity':
        # Sampling: base_sampling_0.5
        if match := re.match(r'base_sampling_([\d.]+)', name):
            return 'Sampling', float(match.group(1)), None, None
        # Top-K: base_top_k_0.3_k50
        elif match := re.match(r'base_top_k_([\d.]+)_k(\d+)', name):
            return 'Top-K', float(match.group(1)), int(match.group(2)), None
        # Top-P: base_top_p_0.9_p0.5
        elif match := re.match(r'base_top_p_([\d.]+)_p([\d.]+)', name):
            return 'Top-P', float(match.group(1)), None, float(match.group(2))
        # Beam: base_beam_5
        elif match := re.match(r'base_beam_(\d+)', name):
            return 'Beam', None, None, int(match.group(1))
        elif 'greedy' in name:
            return 'Greedy', None, None, None
    else:
        # Syntax patterns
        if match := re.match(r'\d+_Sampling_T([\d.]+)', name):
            return 'Sampling', float(match.group(1)), None, None
        elif match := re.match(r'\d+_Top-K_T([\d.]+),_K(\d+)', name):
            return 'Top-K', float(match.group(1)), int(match.group(2)), None
        elif match := re.match(r'\d+_Top-P_T([\d.]+),_P([\d.]+)', name):
            return 'Top-P', float(match.group(1)), None, float(match.group(2))
        elif match := re.match(r'\d+_Beam_Search_beams(\d+)', name):
            return 'Beam', None, None, int(match.group(1))
        elif 'Greedy' in name:
            return 'Greedy', None, None, None
    
    return None, None, None, None

def create_heatmap(data, task_type, output_dir):
    """Create both comprehensive ranking heatmap and strategy-specific matrix heatmaps"""
    
    # First create the comprehensive ranking heatmap (improved)
    create_comprehensive_ranking_heatmap(data, task_type, output_dir)
    
    # Then create strategy-specific matrix heatmaps
    create_strategy_matrix_heatmaps(data, task_type, output_dir)

def create_comprehensive_ranking_heatmap(data, task_type, output_dir):
    """Create compact comprehensive heatmap showing all configurations ranked by ELO"""
    # Extract all configurations with their details
    config_data = []
    
    for result in data:
        strategy, temp, param1, param2 = extract_strategy_info(result['filename'], task_type)
        if strategy:
            # Create readable configuration name
            if strategy == 'Sampling':
                config_name = f"Sampling T={temp}"
            elif strategy == 'Top-K':
                config_name = f"Top-K T={temp} K={param1}"
            elif strategy == 'Top-P':
                config_name = f"Top-P T={temp} P={param2}"
            elif strategy == 'Beam':
                config_name = f"Beam Width={param2}"
            elif strategy == 'Greedy':
                config_name = "Greedy"
            else:
                continue
            
            config_data.append({
                'name': config_name,
                'elo': result['elo'],
                'rank': result['rank'],
                'strategy': strategy
            })
    
    # Sort by rank (best to worst)
    config_data.sort(key=lambda x: x['rank'])
    
    # Create figure with better proportions
    fig, ax = plt.subplots(1, 1, figsize=(14, max(8, len(config_data) * 0.4)))
    
    # Extract data for plotting
    config_names = [item['name'] for item in config_data]
    elos = [item['elo'] for item in config_data]
    ranks = [item['rank'] for item in config_data]
    
    # Create color map based on rank (best=green, worst=red)
    rank_normalized = [(rank - 1) / (max(ranks) - 1) for rank in ranks]
    colors = plt.cm.RdYlGn_r(rank_normalized)  # Reverse so best rank is green
    
    # Create horizontal bar chart
    y_positions = range(len(config_names))
    bars = ax.barh(y_positions, elos, color=colors, edgecolor='black', linewidth=0.5, height=0.8)
    
    # Customize the plot
    ax.set_yticks(y_positions)
    ax.set_yticklabels([f"#{rank} {name}" for rank, name in zip(ranks, config_names)], fontsize=9)
    ax.set_xlabel('ELO Score', fontsize=12, fontweight='bold')
    ax.set_title(f'{task_type.title()} Tournament - All Configurations Ranked by Performance', 
                fontsize=14, fontweight='bold', pad=20)
    
    # Add ELO values on bars
    for i, (bar, elo) in enumerate(zip(bars, elos)):
        ax.text(bar.get_width() + 10, bar.get_y() + bar.get_height()/2, 
               f'{int(elo)}', ha='left', va='center', fontsize=8, fontweight='bold')
    
    # Add colorbar for rank
    sm = plt.cm.ScalarMappable(cmap=plt.cm.RdYlGn_r, 
                              norm=plt.Normalize(vmin=1, vmax=max(ranks)))
    sm.set_array([])
    cbar = plt.colorbar(sm, ax=ax, shrink=0.6)
    cbar.set_label('Rank (1=Best)', fontsize=10, fontweight='bold')
    
    # Adjust layout
    ax.set_xlim(min(elos) - 50, max(elos) + 100)
    ax.grid(axis='x', alpha=0.3)
    ax.invert_yaxis()  # Best rank at top
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, f'{task_type}_comprehensive_ranking.png'), 
                dpi=300, bbox_inches='tight')
    plt.close()

def create_strategy_matrix_heatmaps(data, task_type, output_dir):
    """Create matrix-style heatmaps for each strategy like in the reference image"""
    
    # Organize data by strategy
    strategy_data = defaultdict(lambda: defaultdict(lambda: defaultdict(float)))
    
    for result in data:
        strategy, temp, param1, param2 = extract_strategy_info(result['filename'], task_type)
        if strategy and temp is not None:
            if strategy == 'Top-K' and param1 is not None:
                strategy_data['Top-K'][temp][param1] = result['elo']
            elif strategy == 'Top-P' and param2 is not None:
                strategy_data['Top-P'][temp][param2] = result['elo']
            elif strategy == 'Sampling':
                strategy_data['Sampling'][temp][1] = result['elo']  # Use 1 as dummy param
    
    # Create matrix heatmaps for Top-K and Top-P
    for strategy in ['Top-K', 'Top-P']:
        if strategy not in strategy_data:
            continue
        
        # Get all temperatures and parameters
        temps = sorted(strategy_data[strategy].keys())
        if strategy == 'Top-K':
            all_params = set()
            for temp_data in strategy_data[strategy].values():
                all_params.update(temp_data.keys())
            params = sorted(all_params)
            param_label = 'K Value'
        else:  # Top-P
            all_params = set()
            for temp_data in strategy_data[strategy].values():
                all_params.update(temp_data.keys())
            params = sorted(all_params)
            param_label = 'P Value'
        
        if not temps or not params:
            continue
        
        # Create matrix
        matrix = np.full((len(temps), len(params)), np.nan)
        for i, temp in enumerate(temps):
            for j, param in enumerate(params):
                if param in strategy_data[strategy][temp]:
                    matrix[i, j] = strategy_data[strategy][temp][param]
        
        # Create heatmap
        fig, ax = plt.subplots(1, 1, figsize=(max(8, len(params) * 1.2), max(6, len(temps) * 0.8)))
        
        # Use a mask for missing data
        mask = np.isnan(matrix)
        
        # Create heatmap
        im = ax.imshow(matrix, cmap='RdYlGn', aspect='auto', interpolation='nearest')
        
        # Add colorbar
        cbar = plt.colorbar(im, ax=ax)
        cbar.set_label('ELO Rating', fontsize=12, fontweight='bold')
        
        # Set ticks and labels
        ax.set_xticks(range(len(params)))
        ax.set_xticklabels([f'{param}' for param in params], fontsize=10)
        ax.set_yticks(range(len(temps)))
        ax.set_yticklabels([f'{temp}' for temp in temps], fontsize=10)
        
        # Add text annotations with ELO values
        for i in range(len(temps)):
            for j in range(len(params)):
                if not mask[i, j]:
                    text = ax.text(j, i, f'{int(matrix[i, j])}',
                                 ha="center", va="center", color="black", fontweight='bold', fontsize=10)
        
        # Set labels and title
        ax.set_xlabel(param_label, fontsize=12, fontweight='bold')
        ax.set_ylabel('Temperature', fontsize=12, fontweight='bold')
        ax.set_title(f'{task_type.title()} - {strategy}: Temperature vs {param_label}', 
                    fontsize=14, fontweight='bold')
        
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, f'{task_type}_{strategy.lower()}_matrix_heatmap.png'), 
                   dpi=300, bbox_inches='tight')
        plt.close()
    
    # Create sampling heatmap (temperature only)
    if 'Sampling' in strategy_data:
        temps = sorted(strategy_data['Sampling'].keys())
        elos = [strategy_data['Sampling'][temp][1] for temp in temps]
        
        fig, ax = plt.subplots(1, 1, figsize=(12, 3))
        
        # Create 1D heatmap
        matrix = np.array(elos).reshape(1, -1)
        im = ax.imshow(matrix, cmap='RdYlGn', aspect='auto')
        
        # Add colorbar
        cbar = plt.colorbar(im, ax=ax)
        cbar.set_label('ELO Rating', fontsize=12, fontweight='bold')
        
        # Set ticks and labels
        ax.set_xticks(range(len(temps)))
        ax.set_xticklabels([f'{temp}' for temp in temps], fontsize=10)
        ax.set_yticks([0])
        ax.set_yticklabels(['Sampling'], fontsize=12)
        
        # Add text annotations
        for j, elo in enumerate(elos):
            ax.text(j, 0, f'{int(elo)}', ha="center", va="center", 
                   color="black", fontweight='bold', fontsize=10)
        
        ax.set_xlabel('Temperature', fontsize=12, fontweight='bold')
        ax.set_title(f'{task_type.title()} - Sampling: Temperature vs ELO', 
                    fontsize=14, fontweight='bold')
        
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, f'{task_type}_sampling_matrix_heatmap.png'), 
                   dpi=300, bbox_inches='tight')
        plt.close()
    
    # Create beam search visualization if available
    beam_data = []
    for result in data:
        strategy, temp, param1, param2 = extract_strategy_info(result['filename'], task_type)
        if strategy == 'Beam':
            beam_data.append((param2, result['elo']))
    
    if beam_data:
        beam_data.sort(key=lambda x: x[0])
        beam_widths = [item[0] for item in beam_data]
        beam_elos = [item[1] for item in beam_data]
        
        fig, ax = plt.subplots(1, 1, figsize=(max(8, len(beam_widths) * 1.5), 3))
        
        # Create 1D heatmap for beam search
        matrix = np.array(beam_elos).reshape(1, -1)
        im = ax.imshow(matrix, cmap='RdYlGn', aspect='auto')
        
        # Add colorbar
        cbar = plt.colorbar(im, ax=ax)
        cbar.set_label('ELO Rating', fontsize=12, fontweight='bold')
        
        # Set ticks and labels
        ax.set_xticks(range(len(beam_widths)))
        ax.set_xticklabels([f'{int(width)}' for width in beam_widths], fontsize=10)
        ax.set_yticks([0])
        ax.set_yticklabels(['Beam Search'], fontsize=12)
        
        # Add text annotations
        for j, elo in enumerate(beam_elos):
            ax.text(j, 0, f'{int(elo)}', ha="center", va="center", 
                   color="black", fontweight='bold', fontsize=10)
        
        ax.set_xlabel('Beam Width', fontsize=12, fontweight='bold')
        ax.set_title(f'{task_type.title()} - Beam Search: Width vs ELO', 
                    fontsize=14, fontweight='bold')
        
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, f'{task_type}_beam_matrix_heatmap.png'), 
                   dpi=300, bbox_inches='tight')
        plt.close()

def create_strategy_line_graphs(data, task_type, output_dir):
    """Create line graphs for each strategy showing parameter variations"""
    
    # Organize data by strategy
    strategy_data = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    
    for result in data:
        strategy, temp, param1, param2 = extract_strategy_info(result['filename'], task_type)
        if strategy and temp is not None:
            if strategy == 'Sampling':
                strategy_data[strategy][temp]['temp'].append((temp, result['elo']))
            elif strategy == 'Top-K':
                strategy_data[strategy][param1][temp].append((temp, result['elo']))
            elif strategy == 'Top-P':
                strategy_data[strategy][param2][temp].append((temp, result['elo']))
    
    # Create temperature vs ELO graphs for each strategy
    for strategy in ['Sampling', 'Top-K', 'Top-P']:
        if strategy not in strategy_data:
            continue
        
        if strategy == 'Sampling':
            # Simple temperature vs ELO for sampling
            fig, ax = plt.subplots(1, 1, figsize=(12, 6))
            
            temps = sorted(strategy_data[strategy].keys())
            elos = [strategy_data[strategy][temp]['temp'][0][1] for temp in temps]
            
            ax.plot(temps, elos, 'o-', linewidth=3, markersize=8, color='#2E86AB')
            ax.set_title(f'{strategy} Strategy - Temperature vs ELO ({task_type.title()})', 
                        fontsize=14, fontweight='bold')
            ax.set_xlabel('Temperature', fontsize=12)
            ax.set_ylabel('ELO Score', fontsize=12)
            ax.grid(True, alpha=0.3)
            
            # Highlight best point
            best_idx = elos.index(max(elos))
            ax.plot(temps[best_idx], elos[best_idx], 'ro', markersize=12, 
                   markerfacecolor='red', alpha=0.8)
            ax.annotate(f'Best: T={temps[best_idx]}, ELO={elos[best_idx]}', 
                       xy=(temps[best_idx], elos[best_idx]), xytext=(10, 10), 
                       textcoords='offset points', fontsize=10, fontweight='bold')
            
            plt.tight_layout()
            plt.savefig(os.path.join(output_dir, f'{task_type}_{strategy.lower()}_temperature_vs_elo.png'), 
                       dpi=300, bbox_inches='tight')
            plt.close()
        
        else:
            # For Top-K and Top-P, create separate graphs for each parameter value
            param_values = sorted(strategy_data[strategy].keys())
            
            for param_val in param_values:
                fig, ax = plt.subplots(1, 1, figsize=(12, 6))
                
                temp_data = strategy_data[strategy][param_val]
                temps = sorted(temp_data.keys())
                elos = [temp_data[temp][0][1] for temp in temps]
                
                param_name = 'K' if strategy == 'Top-K' else 'P'
                color = '#FF6B35' if strategy == 'Top-K' else '#A23B72'
                
                ax.plot(temps, elos, 'o-', linewidth=3, markersize=8, color=color)
                ax.set_title(f'{strategy} Strategy ({param_name}={param_val}) - Temperature vs ELO ({task_type.title()})', 
                            fontsize=14, fontweight='bold')
                ax.set_xlabel('Temperature', fontsize=12)
                ax.set_ylabel('ELO Score', fontsize=12)
                ax.grid(True, alpha=0.3)
                
                # Highlight best point
                if elos:
                    best_idx = elos.index(max(elos))
                    ax.plot(temps[best_idx], elos[best_idx], 'ro', markersize=12, 
                           markerfacecolor='red', alpha=0.8)
                    ax.annotate(f'Best: T={temps[best_idx]}, ELO={elos[best_idx]}', 
                               xy=(temps[best_idx], elos[best_idx]), xytext=(10, 10), 
                               textcoords='offset points', fontsize=10, fontweight='bold')
                
                plt.tight_layout()
                plt.savefig(os.path.join(output_dir, f'{task_type}_{strategy.lower()}_{param_name.lower()}{param_val}_temperature_vs_elo.png'), 
                           dpi=300, bbox_inches='tight')
                plt.close()

def create_parameter_vs_elo_graphs(data, task_type, output_dir):
    """Create parameter vs ELO graphs for fixed temperatures"""
    
    # Organize data
    strategy_data = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    
    for result in data:
        strategy, temp, param1, param2 = extract_strategy_info(result['filename'], task_type)
        if strategy and temp is not None:
            if strategy == 'Top-K':
                strategy_data[strategy][temp][param1].append(result['elo'])
            elif strategy == 'Top-P':
                strategy_data[strategy][temp][param2].append(result['elo'])
    
    # Create parameter vs ELO graphs
    for strategy in ['Top-K', 'Top-P']:
        if strategy not in strategy_data:
            continue
        
        temps = sorted(strategy_data[strategy].keys())
        param_name = 'K' if strategy == 'Top-K' else 'P'
        color = '#FF6B35' if strategy == 'Top-K' else '#A23B72'
        
        for temp in temps:
            fig, ax = plt.subplots(1, 1, figsize=(12, 6))
            
            param_data = strategy_data[strategy][temp]
            params = sorted(param_data.keys())
            elos = [param_data[param][0] for param in params]
            
            ax.plot(params, elos, 'o-', linewidth=3, markersize=8, color=color)
            ax.set_title(f'{strategy} Strategy (T={temp}) - {param_name} Value vs ELO ({task_type.title()})', 
                        fontsize=14, fontweight='bold')
            ax.set_xlabel(f'{param_name} Value', fontsize=12)
            ax.set_ylabel('ELO Score', fontsize=12)
            ax.grid(True, alpha=0.3)
            
            # Highlight best point
            if elos:
                best_idx = elos.index(max(elos))
                ax.plot(params[best_idx], elos[best_idx], 'ro', markersize=12, 
                       markerfacecolor='red', alpha=0.8)
                ax.annotate(f'Best: {param_name}={params[best_idx]}, ELO={elos[best_idx]}', 
                           xy=(params[best_idx], elos[best_idx]), xytext=(10, 10), 
                           textcoords='offset points', fontsize=10, fontweight='bold')
            
            plt.tight_layout()
            plt.savefig(os.path.join(output_dir, f'{task_type}_{strategy.lower()}_t{temp}_{param_name.lower()}_vs_elo.png'), 
                       dpi=300, bbox_inches='tight')
            plt.close()

def create_beam_graph(data, task_type, output_dir):
    """Create beam width vs ELO graph"""
    beam_data = []
    
    for result in data:
        strategy, temp, param1, param2 = extract_strategy_info(result['filename'], task_type)
        if strategy == 'Beam':
            beam_data.append((param2, result['elo']))
    
    if not beam_data:
        print(f"No beam search data found for {task_type}")
        return
    
    beam_data.sort(key=lambda x: x[0])
    beam_sizes, elos = zip(*beam_data)
    
    fig, ax = plt.subplots(1, 1, figsize=(12, 6))
    
    ax.plot(beam_sizes, elos, 'o-', linewidth=3, markersize=10, color='#8B4513')
    ax.set_title(f'Beam Search - Beam Width vs ELO ({task_type.title()})', 
                fontsize=14, fontweight='bold')
    ax.set_xlabel('Beam Width', fontsize=12)
    ax.set_ylabel('ELO Score', fontsize=12)
    ax.grid(True, alpha=0.3)
    
    # Highlight best point
    best_idx = elos.index(max(elos))
    ax.plot(beam_sizes[best_idx], elos[best_idx], 'ro', markersize=12, 
           markerfacecolor='red', alpha=0.8)
    ax.annotate(f'Best: Width={beam_sizes[best_idx]}, ELO={elos[best_idx]}', 
               xy=(beam_sizes[best_idx], elos[best_idx]), xytext=(10, 10), 
               textcoords='offset points', fontsize=10, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, f'{task_type}_beam_search_width_vs_elo.png'), 
               dpi=300, bbox_inches='tight')
    plt.close()

def generate_text_analysis(data, task_type, output_dir):
    """Generate detailed text analysis for LLM consumption"""
    
    analysis = []
    analysis.append(f"# {task_type.title()} Tournament Analysis")
    analysis.append(f"Total configurations analyzed: {len(data)}")
    analysis.append("")
    
    # Top performers
    analysis.append("## Top 10 Performers")
    for i, result in enumerate(data[:10], 1):
        analysis.append(f"{i}. {result['filename']} - ELO: {result['elo']}, Win Rate: {result['win_rate']}%, Buchholz: {result['buchholz']}")
    analysis.append("")
    
    # Strategy-wise analysis
    strategy_performance = defaultdict(list)
    for result in data:
        strategy, temp, param1, param2 = extract_strategy_info(result['filename'], task_type)
        if strategy:
            strategy_performance[strategy].append({
                'elo': result['elo'],
                'temp': temp,
                'param1': param1,
                'param2': param2,
                'filename': result['filename']
            })
    
    analysis.append("## Strategy Performance Analysis")
    for strategy in sorted(strategy_performance.keys()):
        results = strategy_performance[strategy]
        avg_elo = sum(r['elo'] for r in results) / len(results)
        max_elo = max(r['elo'] for r in results)
        min_elo = min(r['elo'] for r in results)
        best_config = max(results, key=lambda x: x['elo'])
        
        analysis.append(f"### {strategy} Strategy")
        analysis.append(f"- Configurations: {len(results)}")
        analysis.append(f"- Average ELO: {avg_elo:.1f}")
        analysis.append(f"- ELO Range: {min_elo} - {max_elo}")
        analysis.append(f"- Best Configuration: {best_config['filename']} (ELO: {best_config['elo']})")
        
        if strategy == 'Sampling':
            temp_performance = defaultdict(list)
            for r in results:
                temp_performance[r['temp']].append(r['elo'])
            
            analysis.append("- Temperature Analysis:")
            for temp in sorted(temp_performance.keys()):
                avg_elo_temp = sum(temp_performance[temp]) / len(temp_performance[temp])
                analysis.append(f"  - T={temp}: Avg ELO {avg_elo_temp:.1f}")
        
        elif strategy in ['Top-K', 'Top-P']:
            # Temperature analysis
            temp_performance = defaultdict(list)
            param_performance = defaultdict(list)
            
            for r in results:
                temp_performance[r['temp']].append(r['elo'])
                param_key = r['param1'] if strategy == 'Top-K' else r['param2']
                param_performance[param_key].append(r['elo'])
            
            analysis.append("- Temperature Analysis:")
            for temp in sorted(temp_performance.keys()):
                avg_elo_temp = sum(temp_performance[temp]) / len(temp_performance[temp])
                analysis.append(f"  - T={temp}: Avg ELO {avg_elo_temp:.1f}")
            
            param_name = 'K' if strategy == 'Top-K' else 'P'
            analysis.append(f"- {param_name} Parameter Analysis:")
            for param in sorted(param_performance.keys()):
                avg_elo_param = sum(param_performance[param]) / len(param_performance[param])
                analysis.append(f"  - {param_name}={param}: Avg ELO {avg_elo_param:.1f}")
        
        elif strategy == 'Beam':
            beam_performance = defaultdict(list)
            for r in results:
                beam_performance[r['param2']].append(r['elo'])
            
            analysis.append("- Beam Width Analysis:")
            for width in sorted(beam_performance.keys()):
                avg_elo_beam = sum(beam_performance[width]) / len(beam_performance[width])
                analysis.append(f"  - Width={width}: Avg ELO {avg_elo_beam:.1f}")
        
        analysis.append("")
    
    # Key insights
    analysis.append("## Key Insights")
    
    # Best overall configuration
    best_config = data[0]
    analysis.append(f"1. Best Overall Configuration: {best_config['filename']} with ELO {best_config['elo']}")
    
    # Strategy ranking
    strategy_avg = {}
    for strategy in strategy_performance:
        strategy_avg[strategy] = sum(r['elo'] for r in strategy_performance[strategy]) / len(strategy_performance[strategy])
    
    sorted_strategies = sorted(strategy_avg.items(), key=lambda x: x[1], reverse=True)
    analysis.append("2. Strategy Ranking by Average ELO:")
    for i, (strategy, avg_elo) in enumerate(sorted_strategies, 1):
        analysis.append(f"   {i}. {strategy}: {avg_elo:.1f}")
    
    # Temperature insights
    if 'Sampling' in strategy_performance:
        sampling_results = strategy_performance['Sampling']
        temp_avg = defaultdict(list)
        for r in sampling_results:
            temp_avg[r['temp']].append(r['elo'])
        
        best_temp = max(temp_avg.items(), key=lambda x: sum(x[1])/len(x[1]))
        analysis.append(f"3. Best Temperature for Sampling: {best_temp[0]} (Avg ELO: {sum(best_temp[1])/len(best_temp[1]):.1f})")
    
    analysis.append("")
    
    # Write analysis to file
    with open(os.path.join(output_dir, f'{task_type}_detailed_analysis.txt'), 'w') as f:
        f.write('\n'.join(analysis))
    
    return '\n'.join(analysis)

def main():
    # Create main output directory
    output_base = "Comprehensive_Analysis"
    os.makedirs(output_base, exist_ok=True)
    
    # Process both creativity and syntax results
    for task_type in ['creativity', 'syntax']:
        print(f"Processing {task_type} tournament results...")
        
        # Create task-specific directory
        task_dir = os.path.join(output_base, task_type)
        os.makedirs(task_dir, exist_ok=True)
        
        # Create subdirectories
        heatmap_dir = os.path.join(task_dir, "heatmaps")
        line_graphs_dir = os.path.join(task_dir, "line_graphs")
        param_graphs_dir = os.path.join(task_dir, "parameter_graphs")
        beam_dir = os.path.join(task_dir, "beam_analysis")
        text_dir = os.path.join(task_dir, "text_analysis")
        
        for dir_path in [heatmap_dir, line_graphs_dir, param_graphs_dir, beam_dir, text_dir]:
            os.makedirs(dir_path, exist_ok=True)
        
        # Parse data
        data_file = f"NewAnalysis/{task_type}.txt"
        if not os.path.exists(data_file):
            print(f"Warning: {data_file} not found, skipping {task_type}")
            continue
        
        data = parse_results_file(data_file)
        
        # Generate visualizations
        print(f"  Creating heatmap...")
        create_heatmap(data, task_type, heatmap_dir)
        
        print(f"  Creating strategy line graphs...")
        create_strategy_line_graphs(data, task_type, line_graphs_dir)
        
        print(f"  Creating parameter vs ELO graphs...")
        create_parameter_vs_elo_graphs(data, task_type, param_graphs_dir)
        
        print(f"  Creating beam analysis...")
        create_beam_graph(data, task_type, beam_dir)
        
        print(f"  Generating text analysis...")
        analysis_text = generate_text_analysis(data, task_type, text_dir)
        
        print(f"  {task_type.title()} analysis complete!")
    
    print(f"\nAll analyses complete! Results saved in: {output_base}/")
    print("\nFolder structure created:")
    print("├── creativity/")
    print("│   ├── heatmaps/")
    print("│   ├── line_graphs/")
    print("│   ├── parameter_graphs/")
    print("│   ├── beam_analysis/")
    print("│   └── text_analysis/")
    print("└── syntax/")
    print("    ├── heatmaps/")
    print("    ├── line_graphs/")
    print("    ├── parameter_graphs/")
    print("    ├── beam_analysis/")
    print("    └── text_analysis/")

if __name__ == "__main__":
    main()
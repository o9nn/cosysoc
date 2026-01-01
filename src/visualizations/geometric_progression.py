"""
Geometric Progression Visualizations for Cosmos Systems

Generates visualizations showing:
1. Pascal's Triangle mapping
2. Simplex polytope progression
3. Matula number tree structures
4. Nested tuple expressions
5. Topological surfaces
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, Polygon, FancyArrowPatch
import numpy as np
from pathlib import Path
import math

# Output directory
OUTPUT_DIR = Path("/home/ubuntu/cosysoc/visualizations/geometry")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Color scheme
COLORS = {
    'void': '#1a1a2e',
    'monad': '#16213e',
    'diasect': '#0f3460',
    'triagon': '#e94560',
    'tetrahedron': '#533483',
    'pentachoron': '#00b4d8',
    'background': '#0d1117',
    'text': '#c9d1d9',
    'accent': '#58a6ff',
    'gold': '#ffd700'
}


def create_pascal_triangle():
    """Create Pascal's Triangle visualization showing system mapping."""
    fig, ax = plt.subplots(figsize=(14, 10), facecolor=COLORS['background'])
    ax.set_facecolor(COLORS['background'])
    
    # Pascal's triangle rows for systems 0-5
    rows = [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
        [1, 5, 10, 10, 5, 1]
    ]
    
    system_names = ['System 0: Void', 'System 1: Monad', 'System 2: Diasect',
                    'System 3: Triagon', 'System 4: Tetrahedron', 'System 5: Pentachoron']
    
    system_colors = [COLORS['void'], COLORS['monad'], COLORS['diasect'],
                     COLORS['triagon'], COLORS['tetrahedron'], COLORS['pentachoron']]
    
    max_width = len(rows[-1])
    
    for row_idx, row in enumerate(rows):
        y = 5 - row_idx
        width = len(row)
        start_x = (max_width - width) / 2
        
        for col_idx, val in enumerate(row):
            x = start_x + col_idx
            
            # Draw hexagon for each number
            hex_size = 0.4
            hexagon = patches.RegularPolygon(
                (x, y), numVertices=6, radius=hex_size,
                facecolor=system_colors[row_idx], edgecolor=COLORS['gold'],
                linewidth=2, alpha=0.8
            )
            ax.add_patch(hexagon)
            
            # Add number
            ax.text(x, y, str(val), ha='center', va='center',
                   fontsize=14, fontweight='bold', color=COLORS['text'])
        
        # Add system label
        ax.text(-1.5, y, system_names[row_idx], ha='right', va='center',
               fontsize=11, color=system_colors[row_idx], fontweight='bold')
        
        # Add sum
        ax.text(max_width + 0.5, y, f'Σ = {sum(row)} = 2^{row_idx}',
               ha='left', va='center', fontsize=10, color=COLORS['accent'])
    
    # Title
    ax.text(2.5, 6.5, "Pascal's Triangle → Cosmos Systems", ha='center', va='center',
           fontsize=18, fontweight='bold', color=COLORS['gold'])
    
    ax.text(2.5, 6, "Projective Geometry Coefficients", ha='center', va='center',
           fontsize=12, color=COLORS['text'])
    
    ax.set_xlim(-3, max_width + 2)
    ax.set_ylim(-1, 7.5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'pascal_triangle_systems.png', dpi=150, 
                facecolor=COLORS['background'], bbox_inches='tight')
    plt.close()
    print(f"Saved: {OUTPUT_DIR / 'pascal_triangle_systems.png'}")


def create_simplex_progression():
    """Create visualization of simplex polytope progression."""
    fig, axes = plt.subplots(2, 3, figsize=(15, 10), facecolor=COLORS['background'])
    
    simplex_data = [
        {'name': 'System 0: Void (-1d)', 'dim': -1, 'color': COLORS['void']},
        {'name': 'System 1: Point (0d)', 'dim': 0, 'color': COLORS['monad']},
        {'name': 'System 2: Line (1d)', 'dim': 1, 'color': COLORS['diasect']},
        {'name': 'System 3: Triangle (2d)', 'dim': 2, 'color': COLORS['triagon']},
        {'name': 'System 4: Tetrahedron (3d)', 'dim': 3, 'color': COLORS['tetrahedron']},
        {'name': 'System 5: Pentachoron (4d)', 'dim': 4, 'color': COLORS['pentachoron']}
    ]
    
    for idx, (ax, data) in enumerate(zip(axes.flat, simplex_data)):
        ax.set_facecolor(COLORS['background'])
        ax.set_aspect('equal')
        
        dim = data['dim']
        color = data['color']
        
        if dim == -1:
            # Void - empty circle with dashed border
            circle = Circle((0.5, 0.5), 0.3, fill=False, 
                           edgecolor=color, linestyle='--', linewidth=2)
            ax.add_patch(circle)
            ax.text(0.5, 0.5, '∅', ha='center', va='center', 
                   fontsize=30, color=color)
        
        elif dim == 0:
            # Point
            ax.plot(0.5, 0.5, 'o', markersize=20, color=color)
            ax.text(0.5, 0.3, '1 vertex', ha='center', fontsize=10, color=COLORS['text'])
        
        elif dim == 1:
            # Line segment
            ax.plot([0.2, 0.8], [0.5, 0.5], '-', linewidth=4, color=color)
            ax.plot([0.2, 0.8], [0.5, 0.5], 'o', markersize=12, color=color)
            ax.text(0.5, 0.3, '2 vertices, 1 edge', ha='center', fontsize=10, color=COLORS['text'])
        
        elif dim == 2:
            # Triangle
            triangle = Polygon([(0.5, 0.8), (0.2, 0.3), (0.8, 0.3)],
                              fill=True, facecolor=color, edgecolor=COLORS['gold'],
                              alpha=0.7, linewidth=2)
            ax.add_patch(triangle)
            ax.plot([0.5, 0.2, 0.8], [0.8, 0.3, 0.3], 'o', markersize=10, color=COLORS['gold'])
            ax.text(0.5, 0.15, '3 vertices, 3 edges, 1 face', ha='center', fontsize=9, color=COLORS['text'])
        
        elif dim == 3:
            # Tetrahedron (2D projection)
            # Front face
            triangle1 = Polygon([(0.5, 0.85), (0.15, 0.25), (0.85, 0.25)],
                               fill=True, facecolor=color, edgecolor=COLORS['gold'],
                               alpha=0.5, linewidth=2)
            ax.add_patch(triangle1)
            # Back edges
            ax.plot([0.5, 0.5], [0.85, 0.45], '-', color=COLORS['gold'], linewidth=2, alpha=0.7)
            ax.plot([0.15, 0.5], [0.25, 0.45], '-', color=COLORS['gold'], linewidth=2, alpha=0.7)
            ax.plot([0.85, 0.5], [0.25, 0.45], '-', color=COLORS['gold'], linewidth=2, alpha=0.7)
            # Vertices
            ax.plot([0.5, 0.15, 0.85, 0.5], [0.85, 0.25, 0.25, 0.45], 'o', 
                   markersize=10, color=COLORS['gold'])
            ax.text(0.5, 0.1, '4V, 6E, 4F, 1C', ha='center', fontsize=9, color=COLORS['text'])
        
        elif dim == 4:
            # Pentachoron (2D projection - Schlegel diagram)
            # Outer tetrahedron
            outer = [(0.5, 0.9), (0.1, 0.2), (0.9, 0.2), (0.5, 0.5)]
            for i in range(4):
                for j in range(i+1, 4):
                    ax.plot([outer[i][0], outer[j][0]], [outer[i][1], outer[j][1]], 
                           '-', color=color, linewidth=2, alpha=0.7)
            # Inner point connected to all
            inner = (0.5, 0.45)
            for pt in outer:
                ax.plot([inner[0], pt[0]], [inner[1], pt[1]], 
                       '-', color=COLORS['gold'], linewidth=1.5, alpha=0.5)
            # Vertices
            for pt in outer + [inner]:
                ax.plot(pt[0], pt[1], 'o', markersize=8, color=COLORS['gold'])
            ax.text(0.5, 0.05, '5V, 10E, 10F, 5C, 1H', ha='center', fontsize=9, color=COLORS['text'])
        
        ax.set_title(data['name'], fontsize=12, color=color, fontweight='bold', pad=10)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')
    
    fig.suptitle('Simplex Polytope Progression: Systems 0-5', 
                fontsize=16, fontweight='bold', color=COLORS['gold'], y=0.98)
    
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'simplex_progression.png', dpi=150,
                facecolor=COLORS['background'], bbox_inches='tight')
    plt.close()
    print(f"Saved: {OUTPUT_DIR / 'simplex_progression.png'}")


def create_concurrency_diagram():
    """Create visualization of concurrency levels across systems."""
    fig, ax = plt.subplots(figsize=(14, 8), facecolor=COLORS['background'])
    ax.set_facecolor(COLORS['background'])
    
    systems = [
        {'num': 0, 'conc': -1, 'name': 'Category/Spin', 'element': '0-Sets'},
        {'num': 1, 'conc': 0, 'name': 'Degree/Point', 'element': '1-Nest'},
        {'num': 2, 'conc': 1, 'name': 'Metric/Line', 'element': '2-Vert'},
        {'num': 3, 'conc': 2, 'name': 'Triangle', 'element': '3-Edge'},
        {'num': 4, 'conc': 3, 'name': 'Tetrahedron', 'element': '4-Face'},
        {'num': 5, 'conc': 4, 'name': '2×2 Convolution', 'element': '5-Cell'}
    ]
    
    colors = [COLORS['void'], COLORS['monad'], COLORS['diasect'],
              COLORS['triagon'], COLORS['tetrahedron'], COLORS['pentachoron']]
    
    x_positions = range(len(systems))
    concurrencies = [s['conc'] for s in systems]
    
    # Bar chart
    bars = ax.bar(x_positions, concurrencies, color=colors, edgecolor=COLORS['gold'], linewidth=2)
    
    # Add labels
    for i, (bar, sys) in enumerate(zip(bars, systems)):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height + 0.2,
               f"System {sys['num']}\n{sys['element']}", ha='center', va='bottom',
               fontsize=10, color=colors[i], fontweight='bold')
        ax.text(bar.get_x() + bar.get_width()/2, height/2 if height > 0 else -0.5,
               sys['name'], ha='center', va='center',
               fontsize=9, color=COLORS['text'], rotation=90 if len(sys['name']) > 10 else 0)
    
    ax.axhline(y=0, color=COLORS['text'], linestyle='-', linewidth=0.5, alpha=0.5)
    ax.set_ylabel('Concurrency Level', fontsize=12, color=COLORS['text'])
    ax.set_xlabel('System', fontsize=12, color=COLORS['text'])
    ax.set_title('Concurrency Progression Across Cosmos Systems', 
                fontsize=16, fontweight='bold', color=COLORS['gold'], pad=20)
    
    ax.set_xticks(x_positions)
    ax.set_xticklabels([f'Sys {s["num"]}' for s in systems], color=COLORS['text'])
    ax.tick_params(colors=COLORS['text'])
    
    for spine in ax.spines.values():
        spine.set_color(COLORS['text'])
        spine.set_alpha(0.3)
    
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'concurrency_progression.png', dpi=150,
                facecolor=COLORS['background'], bbox_inches='tight')
    plt.close()
    print(f"Saved: {OUTPUT_DIR / 'concurrency_progression.png'}")


def create_terms_partitions_chart():
    """Create chart showing terms vs partitions relationship."""
    fig, ax = plt.subplots(figsize=(12, 8), facecolor=COLORS['background'])
    ax.set_facecolor(COLORS['background'])
    
    systems = range(6)
    terms = [1, 1, 2, 4, 9, 20]
    partitions = [0, 1, 2, 3, 5, 7]
    
    colors = [COLORS['void'], COLORS['monad'], COLORS['diasect'],
              COLORS['triagon'], COLORS['tetrahedron'], COLORS['pentachoron']]
    
    x = np.arange(len(systems))
    width = 0.35
    
    bars1 = ax.bar(x - width/2, terms, width, label='Terms', color=COLORS['accent'], alpha=0.8)
    bars2 = ax.bar(x + width/2, partitions, width, label='Partitions', color=COLORS['gold'], alpha=0.8)
    
    # Add value labels
    for bar in bars1:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height + 0.3,
               str(int(height)), ha='center', va='bottom', fontsize=11, color=COLORS['accent'])
    
    for bar in bars2:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height + 0.3,
               str(int(height)), ha='center', va='bottom', fontsize=11, color=COLORS['gold'])
    
    ax.set_ylabel('Count', fontsize=12, color=COLORS['text'])
    ax.set_xlabel('System', fontsize=12, color=COLORS['text'])
    ax.set_title('Terms and Partitions per System\n(Related to OEIS A000081)', 
                fontsize=14, fontweight='bold', color=COLORS['gold'], pad=20)
    
    ax.set_xticks(x)
    ax.set_xticklabels([f'System {i}' for i in systems], color=COLORS['text'])
    ax.tick_params(colors=COLORS['text'])
    ax.legend(facecolor=COLORS['background'], edgecolor=COLORS['text'], 
             labelcolor=COLORS['text'])
    
    for spine in ax.spines.values():
        spine.set_color(COLORS['text'])
        spine.set_alpha(0.3)
    
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'terms_partitions.png', dpi=150,
                facecolor=COLORS['background'], bbox_inches='tight')
    plt.close()
    print(f"Saved: {OUTPUT_DIR / 'terms_partitions.png'}")


def create_nested_tuple_visualization():
    """Create visualization of nested tuple expressions."""
    fig, ax = plt.subplots(figsize=(16, 10), facecolor=COLORS['background'])
    ax.set_facecolor(COLORS['background'])
    
    tuples = [
        ('System 0', '—', 'Undefined (void)'),
        ('System 1', '[1] = (1) = | = 1', 'Single element'),
        ('System 2', '[2[1]] = [1,1]', 'Two System 1s'),
        ('System 3', '[3[2[1]]] = [[1,1],[1,1],[1,1]]', 'Three System 2s'),
        ('System 4', '[4[3[2[1]]]] = [[[1,1],[1,1],[1,1]], ...]×4', 'Four System 3s'),
        ('System 5', '[5[4[3[2[1]]]]] = [[...×4], ...]×5', 'Five System 4s')
    ]
    
    colors = [COLORS['void'], COLORS['monad'], COLORS['diasect'],
              COLORS['triagon'], COLORS['tetrahedron'], COLORS['pentachoron']]
    
    y_positions = np.linspace(0.9, 0.1, len(tuples))
    
    for i, ((name, expr, desc), y, color) in enumerate(zip(tuples, y_positions, colors)):
        # System name
        ax.text(0.05, y, name, fontsize=14, fontweight='bold', color=color,
               transform=ax.transAxes, va='center')
        
        # Expression
        ax.text(0.2, y, expr, fontsize=12, color=COLORS['text'], fontfamily='monospace',
               transform=ax.transAxes, va='center')
        
        # Description
        ax.text(0.75, y, desc, fontsize=11, color=COLORS['accent'], style='italic',
               transform=ax.transAxes, va='center')
        
        # Connecting line (using plot instead of axhline to avoid transform issues)
        ax.plot([0.02, 0.98], [y, y], color=color, alpha=0.2, linewidth=1,
               transform=ax.transAxes)
    
    ax.set_title('Nested Tuple Expressions: Recursive System Structure', 
                fontsize=16, fontweight='bold', color=COLORS['gold'], pad=20)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'nested_tuples.png', dpi=150,
                facecolor=COLORS['background'], bbox_inches='tight')
    plt.close()
    print(f"Saved: {OUTPUT_DIR / 'nested_tuples.png'}")


def create_matula_tree_diagram():
    """Create diagram showing Matula number tree structures."""
    fig, axes = plt.subplots(2, 3, figsize=(15, 10), facecolor=COLORS['background'])
    
    matula_data = [
        {'sys': 0, 'nums': [1], 'trees': ['∅'], 'color': COLORS['void']},
        {'sys': 1, 'nums': [2], 'trees': ['●'], 'color': COLORS['monad']},
        {'sys': 2, 'nums': [4, 3], 'trees': ['● ●', '●─●'], 'color': COLORS['diasect']},
        {'sys': 3, 'nums': [8, 6, 7, 5], 'trees': ['● ● ●', '●─● ●', '●<●', '●─●─●'], 'color': COLORS['triagon']},
        {'sys': 4, 'nums': [16, 12, 9, 14, 10, 19, 13, 17, 11], 
         'trees': ['4 sep', '2+nest', '2 pairs', 'bin+1', 'lin+1', 'star', 'mix', 'deep-b', 'deep-l'],
         'color': COLORS['tetrahedron']},
        {'sys': 5, 'nums': [32, 34, 18, '...'], 'trees': ['5 sep', 'complex', '...', '20 total'],
         'color': COLORS['pentachoron']}
    ]
    
    for ax, data in zip(axes.flat, matula_data):
        ax.set_facecolor(COLORS['background'])
        
        nums_str = ', '.join(str(n) for n in data['nums'][:6])
        if len(data['nums']) > 6:
            nums_str += ', ...'
        
        ax.text(0.5, 0.85, f"System {data['sys']}", fontsize=14, fontweight='bold',
               color=data['color'], ha='center', transform=ax.transAxes)
        
        ax.text(0.5, 0.65, f"Matula: {{ {nums_str} }}", fontsize=10,
               color=COLORS['text'], ha='center', transform=ax.transAxes, fontfamily='monospace')
        
        # Draw tree representations
        trees_str = '\n'.join(data['trees'][:4])
        ax.text(0.5, 0.35, trees_str, fontsize=11, color=COLORS['accent'],
               ha='center', va='center', transform=ax.transAxes, fontfamily='monospace')
        
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')
    
    fig.suptitle('Matula Numbers: Prime Factorization Encoding of Rooted Trees', 
                fontsize=16, fontweight='bold', color=COLORS['gold'], y=0.98)
    
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'matula_numbers.png', dpi=150,
                facecolor=COLORS['background'], bbox_inches='tight')
    plt.close()
    print(f"Saved: {OUTPUT_DIR / 'matula_numbers.png'}")


def main():
    """Generate all geometric progression visualizations."""
    print("Generating geometric progression visualizations...")
    
    create_pascal_triangle()
    create_simplex_progression()
    create_concurrency_diagram()
    create_terms_partitions_chart()
    create_nested_tuple_visualization()
    create_matula_tree_diagram()
    
    print(f"\nAll visualizations saved to: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()

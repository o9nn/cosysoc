"""
Cosmos System of Consciousness - Animation Framework

This module provides tools for creating animated visualizations
of the Systems 1-5 framework, including:
- State transitions
- Energy flows
- Geometric transformations
- Enneagram rotations
- Tetrahedral dynamics
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle, Polygon, FancyArrowPatch
from matplotlib.collections import PatchCollection
import math
from typing import List, Tuple, Optional, Callable
from dataclasses import dataclass


# =============================================================================
# CONFIGURATION
# =============================================================================

@dataclass
class AnimationConfig:
    """Configuration for animations"""
    fps: int = 30
    duration: float = 5.0  # seconds
    width: int = 800
    height: int = 600
    dpi: int = 100
    background_color: str = '#1a1a2e'
    primary_color: str = '#e94560'
    secondary_color: str = '#0f3460'
    accent_color: str = '#16213e'
    text_color: str = '#ffffff'


# =============================================================================
# SYSTEM 1: UNIVERSAL WHOLENESS ANIMATION
# =============================================================================

class System1Animator:
    """
    Animate System 1: Concentric circles representing center/periphery.
    
    Shows the unbounded active interface between center and periphery.
    """
    
    def __init__(self, config: AnimationConfig = None):
        self.config = config or AnimationConfig()
        
    def create_animation(self, output_path: str = 'system1_animation.gif'):
        """Create animated visualization of System 1"""
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.set_xlim(-2, 2)
        ax.set_ylim(-2, 2)
        ax.set_aspect('equal')
        ax.set_facecolor(self.config.background_color)
        fig.patch.set_facecolor(self.config.background_color)
        ax.axis('off')
        
        # Create concentric circles
        circles = []
        n_circles = 5
        for i in range(n_circles):
            circle = Circle((0, 0), 0.2 + i * 0.3, fill=False, 
                          color=self.config.primary_color, linewidth=2)
            ax.add_patch(circle)
            circles.append(circle)
        
        # Center point
        center = Circle((0, 0), 0.1, fill=True, 
                        color=self.config.accent_color)
        ax.add_patch(center)
        
        # Title
        title = ax.text(0, 1.8, 'System 1: Universal Wholeness', 
                       ha='center', va='center', fontsize=14,
                       color=self.config.text_color)
        
        def animate(frame):
            # Pulsing effect
            phase = frame / 30 * 2 * np.pi
            for i, circle in enumerate(circles):
                base_radius = 0.2 + i * 0.3
                pulse = 0.05 * np.sin(phase + i * 0.5)
                circle.set_radius(base_radius + pulse)
                alpha = 0.3 + 0.3 * np.sin(phase + i * 0.5)
                circle.set_alpha(alpha)
            return circles
        
        frames = int(self.config.fps * self.config.duration)
        anim = animation.FuncAnimation(fig, animate, frames=frames, 
                                       interval=1000/self.config.fps, blit=True)
        anim.save(output_path, writer='pillow', fps=self.config.fps)
        plt.close()
        return output_path


# =============================================================================
# SYSTEM 2: PERCEPTIVE WHOLENESS ANIMATION
# =============================================================================

class System2Animator:
    """
    Animate System 2: Two centers forming perceptive wholeness.
    
    Shows the oscillation between subjective and objective modes.
    """
    
    def __init__(self, config: AnimationConfig = None):
        self.config = config or AnimationConfig()
    
    def create_animation(self, output_path: str = 'system2_animation.gif'):
        """Create animated visualization of System 2"""
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.set_xlim(-3, 3)
        ax.set_ylim(-2, 2)
        ax.set_aspect('equal')
        ax.set_facecolor(self.config.background_color)
        fig.patch.set_facecolor(self.config.background_color)
        ax.axis('off')
        
        # Two centers
        center1 = Circle((-1, 0), 0.3, fill=True, 
                        color=self.config.primary_color, alpha=0.8)
        center2 = Circle((1, 0), 0.3, fill=True, 
                        color=self.config.secondary_color, alpha=0.8)
        ax.add_patch(center1)
        ax.add_patch(center2)
        
        # Connection line
        line, = ax.plot([-1, 1], [0, 0], color=self.config.text_color, 
                       linewidth=2, alpha=0.5)
        
        # Labels
        ax.text(-1, -0.6, 'Subjective', ha='center', fontsize=10,
               color=self.config.text_color)
        ax.text(1, -0.6, 'Objective', ha='center', fontsize=10,
               color=self.config.text_color)
        ax.text(0, 1.5, 'System 2: Perceptive Wholeness', 
               ha='center', fontsize=14, color=self.config.text_color)
        
        # Energy indicator
        energy_dot = Circle((0, 0), 0.15, fill=True, 
                           color=self.config.accent_color)
        ax.add_patch(energy_dot)
        
        def animate(frame):
            phase = frame / 30 * 2 * np.pi
            
            # Oscillate sizes (energy transfer)
            size1 = 0.3 + 0.1 * np.sin(phase)
            size2 = 0.3 - 0.1 * np.sin(phase)
            center1.set_radius(size1)
            center2.set_radius(size2)
            
            # Move energy indicator
            x_pos = np.sin(phase)
            energy_dot.center = (x_pos, 0)
            
            return [center1, center2, energy_dot]
        
        frames = int(self.config.fps * self.config.duration)
        anim = animation.FuncAnimation(fig, animate, frames=frames,
                                       interval=1000/self.config.fps, blit=True)
        anim.save(output_path, writer='pillow', fps=self.config.fps)
        plt.close()
        return output_path


# =============================================================================
# SYSTEM 3: FOUR RELATIONS ANIMATION
# =============================================================================

class System3Animator:
    """
    Animate System 3: Four relations forming triangular structure.
    
    Shows the four terms: Discretion, Means, Goal, Consequence.
    """
    
    def __init__(self, config: AnimationConfig = None):
        self.config = config or AnimationConfig()
    
    def create_animation(self, output_path: str = 'system3_animation.gif'):
        """Create animated visualization of System 3"""
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.set_xlim(-2, 2)
        ax.set_ylim(-2, 2)
        ax.set_aspect('equal')
        ax.set_facecolor(self.config.background_color)
        fig.patch.set_facecolor(self.config.background_color)
        ax.axis('off')
        
        # Four centers at triangle + center positions
        positions = [
            (0, 1.2),      # Top - Discretion
            (-1, -0.6),    # Bottom left - Means
            (1, -0.6),     # Bottom right - Goal
            (0, 0)         # Center - Consequence
        ]
        labels = ['Discretion', 'Means', 'Goal', 'Consequence']
        colors = ['#e94560', '#0f3460', '#16213e', '#533483']
        
        circles = []
        for i, (pos, label, color) in enumerate(zip(positions, labels, colors)):
            circle = Circle(pos, 0.25, fill=True, color=color, alpha=0.8)
            ax.add_patch(circle)
            circles.append(circle)
            ax.text(pos[0], pos[1] - 0.45, label, ha='center', fontsize=9,
                   color=self.config.text_color)
        
        # Draw triangle edges
        triangle_pts = [positions[0], positions[1], positions[2], positions[0]]
        for i in range(3):
            ax.plot([triangle_pts[i][0], triangle_pts[i+1][0]],
                   [triangle_pts[i][1], triangle_pts[i+1][1]],
                   color=self.config.text_color, linewidth=1, alpha=0.3)
        
        # Connect center to vertices
        for i in range(3):
            ax.plot([positions[3][0], positions[i][0]],
                   [positions[3][1], positions[i][1]],
                   color=self.config.text_color, linewidth=1, alpha=0.3)
        
        ax.text(0, 1.8, 'System 3: Four Relations', 
               ha='center', fontsize=14, color=self.config.text_color)
        
        def animate(frame):
            phase = frame / 30 * 2 * np.pi
            
            # Pulsing effect for each relation
            for i, circle in enumerate(circles):
                pulse = 0.05 * np.sin(phase + i * np.pi/2)
                circle.set_radius(0.25 + pulse)
                alpha = 0.6 + 0.3 * np.sin(phase + i * np.pi/2)
                circle.set_alpha(alpha)
            
            return circles
        
        frames = int(self.config.fps * self.config.duration)
        anim = animation.FuncAnimation(fig, animate, frames=frames,
                                       interval=1000/self.config.fps, blit=True)
        anim.save(output_path, writer='pillow', fps=self.config.fps)
        plt.close()
        return output_path


# =============================================================================
# SYSTEM 4: ENNEAGRAM ANIMATION
# =============================================================================

class System4Animator:
    """
    Animate System 4: Enneagram with nine positions.
    
    Shows the transformation sequence 1→4→2→8→5→7 and mediating triangle.
    """
    
    def __init__(self, config: AnimationConfig = None):
        self.config = config or AnimationConfig()
    
    def _enneagram_positions(self, radius: float = 1.5) -> List[Tuple[float, float]]:
        """Calculate the 9 positions of the enneagram"""
        positions = []
        for i in range(9):
            angle = np.pi/2 - i * 2 * np.pi / 9  # Start from top
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            positions.append((x, y))
        return positions
    
    def create_animation(self, output_path: str = 'system4_animation.gif'):
        """Create animated visualization of System 4"""
        fig, ax = plt.subplots(figsize=(10, 10))
        ax.set_xlim(-2.5, 2.5)
        ax.set_ylim(-2.5, 2.5)
        ax.set_aspect('equal')
        ax.set_facecolor(self.config.background_color)
        fig.patch.set_facecolor(self.config.background_color)
        ax.axis('off')
        
        positions = self._enneagram_positions()
        
        # Draw outer circle
        outer_circle = Circle((0, 0), 1.5, fill=False, 
                             color=self.config.text_color, linewidth=1, alpha=0.3)
        ax.add_patch(outer_circle)
        
        # Six-pointed figure sequence: 1→4→2→8→5→7
        six_sequence = [0, 3, 1, 7, 4, 6]  # 0-indexed
        for i in range(len(six_sequence)):
            j = (i + 1) % len(six_sequence)
            p1, p2 = positions[six_sequence[i]], positions[six_sequence[j]]
            ax.plot([p1[0], p2[0]], [p1[1], p2[1]], 
                   color=self.config.primary_color, linewidth=2, alpha=0.6)
        
        # Mediating triangle: 3→6→9
        triangle_sequence = [2, 5, 8]  # 0-indexed
        for i in range(3):
            j = (i + 1) % 3
            p1, p2 = positions[triangle_sequence[i]], positions[triangle_sequence[j]]
            ax.plot([p1[0], p2[0]], [p1[1], p2[1]], 
                   color=self.config.secondary_color, linewidth=2, alpha=0.6)
        
        # Position circles
        circles = []
        for i, pos in enumerate(positions):
            circle = Circle(pos, 0.15, fill=True, 
                          color=self.config.accent_color, alpha=0.8)
            ax.add_patch(circle)
            circles.append(circle)
            ax.text(pos[0], pos[1], str(i+1), ha='center', va='center',
                   fontsize=10, color=self.config.text_color, fontweight='bold')
        
        ax.text(0, 2.2, 'System 4: Primary Creative Process', 
               ha='center', fontsize=14, color=self.config.text_color)
        
        # Energy flow indicator
        flow_dot = Circle(positions[0], 0.1, fill=True, 
                         color='#ffff00', alpha=0.9)
        ax.add_patch(flow_dot)
        
        def animate(frame):
            # Move flow indicator along six-pointed figure
            cycle_length = 60  # frames per cycle
            progress = (frame % cycle_length) / cycle_length
            
            # Interpolate position along sequence
            seq_pos = progress * len(six_sequence)
            idx = int(seq_pos) % len(six_sequence)
            next_idx = (idx + 1) % len(six_sequence)
            t = seq_pos - int(seq_pos)
            
            p1 = positions[six_sequence[idx]]
            p2 = positions[six_sequence[next_idx]]
            x = p1[0] + t * (p2[0] - p1[0])
            y = p1[1] + t * (p2[1] - p1[1])
            flow_dot.center = (x, y)
            
            # Pulse current position
            for i, circle in enumerate(circles):
                if i == six_sequence[idx]:
                    circle.set_radius(0.15 + 0.05 * (1 - t))
                else:
                    circle.set_radius(0.15)
            
            return circles + [flow_dot]
        
        frames = int(self.config.fps * self.config.duration)
        anim = animation.FuncAnimation(fig, animate, frames=frames,
                                       interval=1000/self.config.fps, blit=True)
        anim.save(output_path, writer='pillow', fps=self.config.fps)
        plt.close()
        return output_path


# =============================================================================
# SYSTEM 5: TETRAHEDRAL ANIMATION
# =============================================================================

class System5Animator:
    """
    Animate System 5: Tetrahedral structure with 4 vertices.
    
    Shows the 3D rotation and concurrent thread phases.
    """
    
    def __init__(self, config: AnimationConfig = None):
        self.config = config or AnimationConfig()
    
    def _project_3d_to_2d(self, point: Tuple[float, float, float], 
                          angle: float) -> Tuple[float, float]:
        """Simple 3D to 2D projection with rotation"""
        x, y, z = point
        # Rotate around Y axis
        x_rot = x * np.cos(angle) - z * np.sin(angle)
        z_rot = x * np.sin(angle) + z * np.cos(angle)
        # Simple perspective projection
        scale = 1 / (3 - z_rot)
        return (x_rot * scale, y * scale)
    
    def create_animation(self, output_path: str = 'system5_animation.gif'):
        """Create animated visualization of System 5"""
        fig, ax = plt.subplots(figsize=(10, 10))
        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-1.5, 1.5)
        ax.set_aspect('equal')
        ax.set_facecolor(self.config.background_color)
        fig.patch.set_facecolor(self.config.background_color)
        ax.axis('off')
        
        # Tetrahedron vertices in 3D
        vertices_3d = [
            (0, 1, 0),           # Top
            (-0.94, -0.33, 0.5), # Bottom left front
            (0.94, -0.33, 0.5),  # Bottom right front
            (0, -0.33, -1)       # Bottom back
        ]
        
        # Labels for vertices
        vertex_labels = ['D-T', 'P-O', 'S-M', 'Core']
        
        ax.text(0, 1.3, 'System 5: Tetrahedral Integration', 
               ha='center', fontsize=14, color=self.config.text_color)
        
        # Create artists
        edge_lines = []
        vertex_circles = []
        vertex_texts = []
        
        def animate(frame):
            ax.clear()
            ax.set_xlim(-1.5, 1.5)
            ax.set_ylim(-1.5, 1.5)
            ax.set_facecolor(self.config.background_color)
            ax.axis('off')
            
            angle = frame / 30 * np.pi / 2  # Slow rotation
            
            # Project vertices
            vertices_2d = [self._project_3d_to_2d(v, angle) for v in vertices_3d]
            
            # Draw edges
            edges = [(0,1), (0,2), (0,3), (1,2), (1,3), (2,3)]
            for i, j in edges:
                p1, p2 = vertices_2d[i], vertices_2d[j]
                ax.plot([p1[0], p2[0]], [p1[1], p2[1]], 
                       color=self.config.text_color, linewidth=2, alpha=0.5)
            
            # Draw vertices
            colors = ['#e94560', '#0f3460', '#16213e', '#533483']
            for i, (pos, label, color) in enumerate(zip(vertices_2d, vertex_labels, colors)):
                circle = Circle(pos, 0.12, fill=True, color=color, alpha=0.9)
                ax.add_patch(circle)
                ax.text(pos[0], pos[1] - 0.2, label, ha='center', fontsize=9,
                       color=self.config.text_color)
            
            # Phase indicators for 3 concurrent streams
            phase = frame / 30 * 2 * np.pi
            for stream in range(3):
                stream_phase = phase + stream * 2 * np.pi / 3
                x = 1.2 * np.cos(stream_phase)
                y = -1.2 + 0.1 * np.sin(stream_phase)
                ax.plot(x, y, 'o', color=['#ff6b6b', '#4ecdc4', '#45b7d1'][stream],
                       markersize=8, alpha=0.8)
            
            ax.text(0, 1.3, 'System 5: Tetrahedral Integration', 
                   ha='center', fontsize=14, color=self.config.text_color)
            ax.text(0, -1.4, '3 Concurrent Streams (120° apart)', 
                   ha='center', fontsize=10, color=self.config.text_color, alpha=0.7)
            
            return []
        
        frames = int(self.config.fps * self.config.duration)
        anim = animation.FuncAnimation(fig, animate, frames=frames,
                                       interval=1000/self.config.fps, blit=False)
        anim.save(output_path, writer='pillow', fps=self.config.fps)
        plt.close()
        return output_path


# =============================================================================
# MAIN GENERATOR
# =============================================================================

def generate_all_animations(output_dir: str = './animations'):
    """Generate all system animations"""
    import os
    os.makedirs(output_dir, exist_ok=True)
    
    config = AnimationConfig()
    
    print("Generating System 1 animation...")
    System1Animator(config).create_animation(f'{output_dir}/system1_animation.gif')
    
    print("Generating System 2 animation...")
    System2Animator(config).create_animation(f'{output_dir}/system2_animation.gif')
    
    print("Generating System 3 animation...")
    System3Animator(config).create_animation(f'{output_dir}/system3_animation.gif')
    
    print("Generating System 4 animation...")
    System4Animator(config).create_animation(f'{output_dir}/system4_animation.gif')
    
    print("Generating System 5 animation...")
    System5Animator(config).create_animation(f'{output_dir}/system5_animation.gif')
    
    print(f"All animations saved to {output_dir}/")


if __name__ == "__main__":
    generate_all_animations('/home/ubuntu/cosysoc/animations')

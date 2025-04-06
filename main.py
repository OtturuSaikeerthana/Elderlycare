import sys
sys.path.append(r"e:\Accenturehack")

import asyncio
from agents import (
    OrchestratorAgent,
    HealthMonitorAgent,
    SafetyMonitorAgent,
    ReminderAgent,
    CommunicationAgent,
    HealthData,
    MovementData,
    AgentMessage
)
import logging
from datetime import datetime
import sys
import random
import numpy as np

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ElderlyCareSystem:
    def __init__(self):
        # Fast initialization of agents
        self.orchestrator = OrchestratorAgent()
        self.health_monitor = HealthMonitorAgent("health_monitor_1")
        self.safety_monitor = SafetyMonitorAgent("safety_monitor_1")
        self.reminder = ReminderAgent("reminder_1")
        self.communication = CommunicationAgent("communication_1")
        
        # Store agents in a dictionary for easy access
        self.agents = {
            "orchestrator": self.orchestrator,
            "health_monitor": self.health_monitor,
            "safety_monitor": self.safety_monitor,
            "reminder": self.reminder,
            "communication": self.communication
        }

    async def initialize(self):
        """Initialize all agents and register them with the orchestrator"""
        logger.info("Initializing Elderly Care System...")
        
        try:
            
            # Register all agents with the orchestrator
            for agent_id, agent in self.agents.items():
                if agent_id != "orchestrator":
                    logger.info(f"Initializing agent: {agent_id}")  # Add this line here
                await self.orchestrator.register_agent(agent_id, agent_id, agent)
            
            logger.info("All agents registered successfully")
        except Exception as e:
            logger.error(f"Error during initialization: {e}")
            raise

    async def start(self):
    
        logger.info("Starting Elderly Care System...")
        
        try:
            # Start the orchestrator
            logger.info("Starting orchestrator...")
            await self.orchestrator.start()
            logger.info("Orchestrator started successfully")
            
            # Start other agents
            for agent_id, agent in self.agents.items():
                if agent_id != "orchestrator":
                    logger.info(f"Attempting to start agent: {agent_id}")
                    await agent.start()  # Debug if this fails
                    logger.info(f"Agent {agent_id} started successfully")
            
            logger.info("System started successfully")
        except Exception as e:
            logger.error(f"Error during startup: {e}")
            raise

    async def stop(self):
        """Stop all agents and clean up resources"""
        logger.info("Stopping Elderly Care System...")
        
        try:
            # Stop all agents
            for agent in self.agents.values():
                if hasattr(agent, 'cleanup'):
                    await agent.cleanup()
            
            logger.info("System stopped successfully")
        except Exception as e:
            logger.error(f"Error during shutdown: {e}")

    async def simulate_health_data(self, user_id: str):
        """Simulate health data with minimal delay"""
        try:
            while True:
                health_data = HealthData(
                    user_id=user_id,
                    heart_rate=random.uniform(60, 100),
                    blood_pressure={
                        "systolic": random.uniform(110, 140),
                        "diastolic": random.uniform(70, 90)
                    },
                    blood_glucose=random.uniform(70, 180),
                    oxygen_level=random.uniform(95, 100)
                )
                await self.health_monitor.process_health_data(health_data)
                await asyncio.sleep(0.5)  # Reduced to 0.5 seconds
        except Exception as e:
            logger.error(f"Error in health data simulation: {e}")

    async def simulate_movement_data(self, user_id: str):
        """Simulate movement data with minimal delay"""
        try:
            while True:
                movement_data = MovementData(
                    user_id=user_id,
                    acceleration={
                        "x": random.uniform(-1, 1),
                        "y": random.uniform(-1, 1),
                        "z": random.uniform(0, 2)
                    },
                    position={
                        "x": random.uniform(0, 10),
                        "y": random.uniform(0, 10),
                        "z": random.uniform(0, 2)
                    },
                    activity_level=random.uniform(0, 1)
                )
                await self.safety_monitor.process_movement_data(movement_data)
                await asyncio.sleep(0.25)  # Reduced to 0.25 seconds
        except Exception as e:
            logger.error(f"Error in movement data simulation: {e}")

def generate_sample_health_data(n=5):
    """Generate n sample health data records"""
    data = []
    for i in range(n):
        data.append(HealthData(
            user_id=f"user_{i+1}",
            heart_rate=random.uniform(60, 100),
            blood_pressure={
                "systolic": random.uniform(110, 140),
                "diastolic": random.uniform(70, 90)
            },
            blood_glucose=random.uniform(70, 180),
            oxygen_level=random.uniform(95, 100),
            timestamp=datetime.now()
        ))
    return data

def generate_sample_movement_data(n=5):
    """Generate n sample movement data records"""
    data = []
    for i in range(n):
        data.append(MovementData(
            user_id=f"user_{i+1}",
            acceleration={
                "x": random.uniform(-1, 1),
                "y": random.uniform(-1, 1),
                "z": random.uniform(0, 2)
            },
            position={
                "x": random.uniform(0, 10),
                "y": random.uniform(0, 10),
                "z": random.uniform(0, 2)
            },
            activity_level=random.uniform(0, 1),
            timestamp=datetime.now()
        ))
    return data

def print_health_data(data):
    """Print health data in a formatted table"""
    print("\nHealth Data Sample:")
    print("=" * 110)
    print(f"{'User ID':<10} {'Heart Rate':<12} {'Blood Pressure':<20} {'Glucose':<10} {'Oxygen':<10} {'Timestamp':<30}")
    print("=" * 110)
    for record in data:
        bp = f"{record.blood_pressure['systolic']:.1f}/{record.blood_pressure['diastolic']:.1f}"
        print(f"{record.user_id:<10} {record.heart_rate:<12.1f} {bp:<20} {record.blood_glucose:<10.1f} {record.oxygen_level:<10.1f} {record.timestamp}")
    
    # Add summary statistics
    print("-" * 110)
    avg_hr = sum(r.heart_rate for r in data) / len(data)
    avg_sys = sum(r.blood_pressure['systolic'] for r in data) / len(data)
    avg_dia = sum(r.blood_pressure['diastolic'] for r in data) / len(data)
    avg_glucose = sum(r.blood_glucose for r in data) / len(data)
    avg_oxygen = sum(r.oxygen_level for r in data) / len(data)
    print(f"AVERAGE:   {avg_hr:<12.1f} {avg_sys:.1f}/{avg_dia:.1f}{' '*16} {avg_glucose:<10.1f} {avg_oxygen:<10.1f}")

def print_movement_data(data):
    """Print movement data in a formatted table"""
    print("\nMovement Data Sample:")
    print("=" * 140)
    print(f"{'User ID':<10} {'Acceleration (x,y,z)':<35} {'Position (x,y,z)':<35} {'Activity':<10} {'Timestamp':<30}")
    print("=" * 140)
    for record in data:
        acc = f"({record.acceleration['x']:6.2f}, {record.acceleration['y']:6.2f}, {record.acceleration['z']:6.2f})"
        pos = f"({record.position['x']:6.2f}, {record.position['y']:6.2f}, {record.position['z']:6.2f})"
        print(f"{record.user_id:<10} {acc:<35} {pos:<35} {record.activity_level:<10.2f} {record.timestamp}")
    
    # Add summary statistics
    print("-" * 140)
    avg_acc_x = sum(r.acceleration['x'] for r in data) / len(data)
    avg_acc_y = sum(r.acceleration['y'] for r in data) / len(data)
    avg_acc_z = sum(r.acceleration['z'] for r in data) / len(data)
    avg_pos_x = sum(r.position['x'] for r in data) / len(data)
    avg_pos_y = sum(r.position['y'] for r in data) / len(data)
    avg_pos_z = sum(r.position['z'] for r in data) / len(data)
    avg_activity = sum(r.activity_level for r in data) / len(data)
    avg_acc = f"({avg_acc_x:6.2f}, {avg_acc_y:6.2f}, {avg_acc_z:6.2f})"
    avg_pos = f"({avg_pos_x:6.2f}, {avg_pos_y:6.2f}, {avg_pos_z:6.2f})"
    print(f"AVERAGE:   {avg_acc:<35} {avg_pos:<35} {avg_activity:<10.2f}")

def load_and_display_datasets(n_samples=10):  # Increased to 10 samples
    """Load and display both health and movement datasets"""
    print("\n" + "="*50)
    print("COMPLETE DATASET OVERVIEW")
    print("="*50)
    
    # Generate sample data
    health_data = generate_sample_health_data(n_samples)
    movement_data = generate_sample_movement_data(n_samples)
    
    # Display the data
    print_health_data(health_data)
    print_movement_data(movement_data)
    
    return health_data, movement_data

async def main():
    system = ElderlyCareSystem()
    
    try:
        logger.info("Initializing and starting the system...")
        
        # Fast parallel initialization
        init_task = system.initialize()
        start_task = system.start()
        await asyncio.gather(init_task, start_task)
        
        logger.info("System initialization and startup completed")
        
        # Start simulation tasks immediately
        user_id = "user_1"
        simulation_tasks = [
            system.simulate_health_data(user_id),
            system.simulate_movement_data(user_id)
        ]
        
        # Run simulation tasks
        await asyncio.gather(*simulation_tasks)
        
    except KeyboardInterrupt:
        logger.info("Received shutdown signal")
    except Exception as e:
        logger.error(f"System error: {e}")
    finally:
        await system.stop()

if __name__ == "__main__":
    try:
        # Quick initialization
        print("\n=== Fast System Startup ===")
        system = ElderlyCareSystem()
        
        # Run the main system immediately
        print("Starting system...")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nProgram terminated by user")
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        sys.exit(1) 
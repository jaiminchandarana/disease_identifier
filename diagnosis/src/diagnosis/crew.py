from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class Diagnosis():
    """Diagnosis crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def extracter1(self) -> Agent:
        return Agent(
            config=self.agents_config['extracter1'], 
            verbose=True
        )
        
    @agent
    def extracter2(self) -> Agent:
        return Agent(
            config=self.agents_config['extracter2'], 
            verbose=True
        )

    @agent
    def disease(self) -> Agent:
        return Agent(
            config=self.agents_config['disease'], 
            verbose=True
        )

    @agent
    def diagnosis(self) -> Agent:
        return Agent(
            config=self.agents_config['diagnosis'],
            verbose=True
        )
        
    @task
    def extract_task1(self) -> Task:
        return Task(
            config=self.tasks_config['extract_task1'], 
        )
        
    @task
    def extract_task2(self) -> Task:
        return Task(
            config=self.tasks_config['extract_task2'], 
        )

    @task
    def disease_task(self) -> Task:
        return Task(
            config=self.tasks_config['disease_task'],
        )

    @task
    def diagnosis_task(self) -> Task:
        return Task(
            config=self.tasks_config['diagnosis_task'],
        )
    
    @crew
    def crew(self) -> Crew:
        """Creates the Diagnosis crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks, 
            process=Process.sequential,
            verbose=True,
        )

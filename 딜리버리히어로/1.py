from typing import List, Text


class NoAgentFoundException(Exception):
    def __init__(self):
        super().__init__("No agent found")


class Agent(object):
    def __init__(self, name, skills, load):
        self.name = name
        self.skills = skills
        self.load = load

    def __str__(self):
        return "<Agent: {}>".format(self.name)


class Ticket(object):
    def __init__(self, id, restrictions):
        self.id = id
        self.restrictions = restrictions


class FinderPolicy(object):
    def _filter_loaded_agents(self, agents: List[Agent]) -> List[Agent]:
        for i in agents[:]:
            if i.load >= 3:
                agents.remove(i)
        if not agents:
            raise NoAgentFoundException

    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        temp_arr = []

        for agent in agents:
            for tech in agent.skills:
                if tech in ticket.restrictions:
                    temp_arr.append(agent)
        if not temp_arr:
            raise NoAgentFoundException
        else:
            return temp_arr


class LeastLoadedAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        super()._filter_loaded_agents(agents)
        obj_agents = super().find(ticket, agents)
        available_agent = sorted(obj_agents, key=lambda agent: (len(agent.skills), agent.load))[0]
        print(available_agent)


class LeastFlexibleAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        super()._filter_loaded_agents(agents)
        obj_agents = super().find(ticket, agents)
        available_agent = sorted(obj_agents, key=lambda agent: (len(agent.skills), agent.load))[0]
        print(available_agent)


ticket = Ticket(id="1", restrictions=["Kor"])
agent1 = Agent(name="A", skills=["English"], load=2)
agent2 = Agent(name="B", skills=["English", "Kor"], load=2)
agent3 = Agent(name="C", skills=["English", "Japanese"], load=2)
agent4 = Agent(name="D", skills=["English", "Japanese"], load=2)
agent5 = Agent(name="E", skills=["English", "Japanese"], load=1)

least_loaded_policy = LeastLoadedAgent()
# returns the Agent with name "B" because of their currently lower load.
least_loaded_policy.find(ticket, [agent1, agent2,agent3,agent4,agent5])

least_flexible_policy = LeastFlexibleAgent()
# returns the Agent with name "A" because of their lower flexibility.
least_flexible_policy.find(ticket, [agent1, agent2,agent3,agent4,agent5])
from agents import (
        compare_agents,
        loc_A,
        loc_B,
        ReflexVacuumAgent,
        TrivialVacuumEnvironment,
        )
from utils import (
        mean,
        )


# Exercise 2.7
print "\n\nExercise 2.7"
n=100
steps=4
print "Compare ReflexVacuumAgent against {n} TrivialVacuumEnvironment instances and {steps} steps".format(**locals())
print compare_agents(TrivialVacuumEnvironment, [ReflexVacuumAgent], n=n, steps=4)

# Exercise 2.8
# Run the environment simulator with a simple reflex agent for all possible
# initial dirt configurations and agent locations
print "\n\nExercise 2.8"
scores = []
for loc_A_status in ('Clean', 'Dirty'):
    for loc_B_status in ('Clean', 'Dirty'):
        for agent_loc in (loc_A, loc_B):
            agent = ReflexVacuumAgent()
            env = TrivialVacuumEnvironment(loc_A_status, loc_B_status)
            env.add_thing(agent, agent_loc)
            env.run(steps)
            scores.append(agent.performance)
            print "Environment=({loc_A_status}, {loc_B_status}) and agent at {agent_loc}, agent scored {agent.performance} in {steps} steps".format(**locals())
print "Mean score {}".format(mean(scores))

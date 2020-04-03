from headers import *
sys.path.append("/private/home/tanmayshankar/Research/Code/spinningup")
from spinup.exercises.pytorch.problem_set_1 import exercise1_1
from spinup.exercises.pytorch.problem_set_1 import exercise1_2_auxiliary
from spinup.utils.run_utils import ExperimentGrid
from PolicyNetworks import mlp, MLPGaussianActor
from spinup import ppo_pytorch as ppo
from spinup.exercises.common import print_result
from functools import partial
import gym, os, pandas as pd, psutil, time
import robosuite
from robosuite.wrappers import GymWrapper

"""
This file runs the OpenAI Spinning Up PPO baseline on all of the Robosuite environments. 
"""

if __name__ == '__main__':
    """
    Run this file to verify your solution.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('--env', dest='env_name', type=str, default='SawyerLift',                   help='Specify the environment name of the Robosuite environment to run PPO On.')
    parser.add_argument('--run_name', dest='run_name', type=str,                                    help='Set the name of the run.')
    parser.add_argument('--train', dest='train', default=True, action='store_true',                 help='Whether to train or evaluate.')
    args = parser.parse_args()

    # Remember, the environment names need to be from here. 
    # environment_names = ["SawyerLift", "SawyerStack", "BaxterLift", "BaxterPegInHole"]
    # environment_names = ["SawyerPickPlaceBread","SawyerPickPlaceCan","SawyerPickPlaceCereal","SawyerPickPlace","SawyerPickPlaceMilk","SawyerNutAssembly", "SawyerNutAssemblyRound","SawyerNutAssemblySquare"]

    # First make the robosuite environment. 
    base_env = robosuite.make(args.env_name, has_renderer=False, use_camera_obs=False, reward_shaping=True)
    # Now make a GymWrapped version of that environment.
    gym_env = GymWrapper(base_env)

    # Create a log directory.
    # logdir = "/tmp/experiments/%i"%int(time.time())
    # logdir = "/tmp/experiments/{0}".format(args.env_name+"_"+args.run_name)
    logdir = "Logs/{0}".format(args.env_name+"_"+args.run_name)

    # Create a policy / critic. 
    ActorCritic = partial(exercise1_2_auxiliary.ExerciseActorCritic, actor=MLPGaussianActor)

    if args.train:
        print("Beginning Training.")
        # Actually call PPO.
        ppo(env_fn = lambda : gym_env,
            actor_critic=ActorCritic,
            ac_kwargs=dict(hidden_sizes=(64,)),
            steps_per_epoch=4000, epochs=100, logger_kwargs=dict(output_dir=logdir))

        # Get scores from last five epochs to evaluate success.
        data = pd.read_table(os.path.join(logdir,'progress.txt'))
        last_scores = data['AverageEpRet'][-5:]

        print("####################")
        # print_result(last_scores)
        print(last_scores)
    else: 
        print("Evaluating, not training.")

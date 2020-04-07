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
from spinup.utils.test_policy import load_policy_and_env, run_policy, render_episode
import imageio 

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
    # parser.add_argument('--train', dest='train', default=True, action='store_true',                 help='Whether to train or evaluate.')
    feature_parser = parser.add_mutually_exclusive_group(required=False)
    feature_parser.add_argument('--train', dest='train', action='store_true')
    feature_parser.add_argument('--no-train', dest='train', action='store_false')
    parser.set_defaults(train=True)
    parser.add_argument('--model', dest='model', type=str,                                          help='Model to load.')

    parser.add_argument('--render', dest='render', type=int, default=1,                             help='Whether to render an episode.')
    parser.add_argument('--evaluate', dest='evaluate', type=int, default=1,                                help='Whether to evaluate.')

    args = parser.parse_args()

    # Remember, the environment names need to be from here. 
    # environment_names = ["SawyerLift", "SawyerStack", "BaxterLift", "BaxterPegInHole"]
    # environment_names = ["SawyerPickPlaceBread","SawyerPickPlaceCan","SawyerPickPlaceCereal","SawyerPickPlace","SawyerPickPlaceMilk","SawyerNutAssembly", "SawyerNutAssemblyRound","SawyerNutAssemblySquare"]

    # First make the robosuite environment. 
    # if args.train:
    base_env = robosuite.make(args.env_name, has_renderer=False, use_camera_obs=False, reward_shaping=True)
    # else:
    #     base_env = robosuite.make(args.env_name, has_renderer=True, use_camera_obs=False, reward_shaping=True)

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

        # Now evaluate last model over 100 episodes. 
        # Load model while evaluating. 
        _ , policy = load_policy_and_env(logdir)

        # Now run the policy.
        run_policy(gym_env, policy, render=False)

        # sim.render(600,600, camera_name='frontview')

    else: 
        print("Evaluating, not training.")

        # Load model while evaluating. 
        if args.model is None: 
            _ , policy = load_policy_and_env(logdir)
        else:
            _ , policy = load_policy_and_env(args.model)

        if render: 
            # Render an episode of the policy. 
            episode_gif = render_episode(gym_env, policy)
            path = os.path.join(logdir, "Images")
            if not(os.path.isdir(path)):
                os.mkdir(path)

            imageio.mimsave(os.path.join(path,"Trained_Rollout"), episode_gif)

        if evaluate:
            # Now run the policy.
            run_policy(gym_env, policy, render=False)
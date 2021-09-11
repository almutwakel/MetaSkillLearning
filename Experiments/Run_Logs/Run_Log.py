# Execute from MetaSkillLearning/Experiments directory: 

# Debug
python Run_Robosuite_PPO.py --env="SawyerLift" --run_name="debug"

# Run
python cluster_run.py --partition=learnfair --name=RL001 --cmd='python Run_Robosuite_PPO.py --env="SawyerLift" --run_name="2"'

python cluster_run.py --partition=learnfair --name=RL002 --cmd='python Run_Robosuite_PPO.py --env="SawyerStack" --run_name="2"'

python cluster_run.py --partition=learnfair --name=RL003 --cmd='python Run_Robosuite_PPO.py --env="SawyerPickPlace" --run_name="2"'

python cluster_run.py --partition=learnfair --name=RL004 --cmd='python Run_Robosuite_PPO.py --env="SawyerNutAssembly" --run_name="2"'

python cluster_run.py --partition=learnfair --name=RL005 --cmd='python Run_Robosuite_PPO.py --env="BaxterLift" --run_name="2"'

python cluster_run.py --partition=learnfair --name=RL006 --cmd='python Run_Robosuite_PPO.py --env="BaxterPegInHole" --run_name="2"'

python cluster_run.py --partition=learnfair --name=RL007 --cmd='python Run_Robosuite_PPO.py --env="SawyerPickPlaceBread" --run_name="2"'

python cluster_run.py --partition=learnfair --name=RL008 --cmd='python Run_Robosuite_PPO.py --env="SawyerPickPlaceCan" --run_name="2"'

python cluster_run.py --partition=learnfair --name=RL009 --cmd='python Run_Robosuite_PPO.py --env="SawyerPickPlaceCereal" --run_name="2"'

python cluster_run.py --partition=learnfair --name=RL010 --cmd='python Run_Robosuite_PPO.py --env="SawyerPickPlaceMilk" --run_name="2"'

python cluster_run.py --partition=learnfair --name=RL011 --cmd='python Run_Robosuite_PPO.py --env="SawyerNutAssemblyRound" --run_name="2"'

python cluster_run.py --partition=learnfair --name=RL012 --cmd='python Run_Robosuite_PPO.py --env="SawyerNutAssemblySquare" --run_name="2"'

# Eval

# Debug
python Run_Robosuite_PPO.py --env="SawyerLift" --run_name="2" --no-train

python cluster_run.py --partition=learnfair --name=RL001 --cmd='python Run_Robosuite_PPO.py --env="SawyerLift" --run_name="2" --no-train'

python cluster_run.py --partition=learnfair --name=RL002 --cmd='python Run_Robosuite_PPO.py --env="SawyerStack" --run_name="2" --no-train'

python cluster_run.py --partition=learnfair --name=RL003 --cmd='python Run_Robosuite_PPO.py --env="SawyerPickPlace" --run_name="2" --no-train'

python cluster_run.py --partition=learnfair --name=RL004 --cmd='python Run_Robosuite_PPO.py --env="SawyerNutAssembly" --run_name="2" --no-train'

python cluster_run.py --partition=learnfair --name=RL005 --cmd='python Run_Robosuite_PPO.py --env="BaxterLift" --run_name="2" --no-train'

python cluster_run.py --partition=learnfair --name=RL006 --cmd='python Run_Robosuite_PPO.py --env="BaxterPegInHole" --run_name="2" --no-train'

python cluster_run.py --partition=learnfair --name=RL007 --cmd='python Run_Robosuite_PPO.py --env="SawyerPickPlaceBread" --run_name="2" --no-train'

python cluster_run.py --partition=learnfair --name=RL008 --cmd='python Run_Robosuite_PPO.py --env="SawyerPickPlaceCan" --run_name="2" --no-train'

python cluster_run.py --partition=learnfair --name=RL009 --cmd='python Run_Robosuite_PPO.py --env="SawyerPickPlaceCereal" --run_name="2" --no-train'

python cluster_run.py --partition=learnfair --name=RL010 --cmd='python Run_Robosuite_PPO.py --env="SawyerPickPlaceMilk" --run_name="2" --no-train'

python cluster_run.py --partition=learnfair --name=RL011 --cmd='python Run_Robosuite_PPO.py --env="SawyerNutAssemblyRound" --run_name="2" --no-train'

python cluster_run.py --partition=learnfair --name=RL012 --cmd='python Run_Robosuite_PPO.py --env="SawyerNutAssemblySquare" --run_name="2" --no-train'

# Viz

# Eval

# Debug
python Run_Robosuite_PPO.py --env="SawyerLift" --run_name="2" --no-train --evaluate=0

python cluster_run.py --partition=learnfair --name=RL001_render --cmd='python Run_Robosuite_PPO.py --env="SawyerLift" --run_name="2" --no-train --evaluate=0'

python cluster_run.py --partition=learnfair --name=RL002_render --cmd='python Run_Robosuite_PPO.py --env="SawyerStack" --run_name="2" --no-train --evaluate=0'

python cluster_run.py --partition=learnfair --name=RL003_render --cmd='python Run_Robosuite_PPO.py --env="SawyerPickPlace" --run_name="2" --no-train --evaluate=0'

python cluster_run.py --partition=learnfair --name=RL004_render --cmd='python Run_Robosuite_PPO.py --env="SawyerNutAssembly" --run_name="2" --no-train --evaluate=0'

python cluster_run.py --partition=learnfair --name=RL005_render --cmd='python Run_Robosuite_PPO.py --env="BaxterLift" --run_name="2" --no-train --evaluate=0'

python cluster_run.py --partition=learnfair --name=RL006_render --cmd='python Run_Robosuite_PPO.py --env="BaxterPegInHole" --run_name="2" --no-train --evaluate=0'

python cluster_run.py --partition=learnfair --name=RL007_render --cmd='python Run_Robosuite_PPO.py --env="SawyerPickPlaceBread" --run_name="2" --no-train --evaluate=0'

python cluster_run.py --partition=learnfair --name=RL008_render --cmd='python Run_Robosuite_PPO.py --env="SawyerPickPlaceCan" --run_name="2" --no-train --evaluate=0'

python cluster_run.py --partition=learnfair --name=RL009_render --cmd='python Run_Robosuite_PPO.py --env="SawyerPickPlaceCereal" --run_name="2" --no-train --evaluate=0'

python cluster_run.py --partition=learnfair --name=RL010_render --cmd='python Run_Robosuite_PPO.py --env="SawyerPickPlaceMilk" --run_name="2" --no-train --evaluate=0'

python cluster_run.py --partition=learnfair --name=RL011_render --cmd='python Run_Robosuite_PPO.py --env="SawyerNutAssemblyRound" --run_name="2" --no-train --evaluate=0'

python cluster_run.py --partition=learnfair --name=RL012_render --cmd='python Run_Robosuite_PPO.py --env="SawyerNutAssemblySquare" --run_name="2" --no-train --evaluate=0'


# Running Hierarchical PPO to debug. 
python Run_Robosuite_PPO.py --env="SawyerLift" --run_name="hierarchy_debug" --hierarchical=1 

# Running Hierarchical PPO on all environments. 
python cluster_run.py --partition=learnfair --name=HRL001 --cmd='python Run_Robosuite_PPO.py --run_name="HRL001" --hierarchical=1 --env="SawyerLift"'

python cluster_run.py --partition=learnfair --name=HRL002 --cmd='python Run_Robosuite_PPO.py --run_name="HRL002" --hierarchical=1 --env="SawyerStack"'

python cluster_run.py --partition=learnfair --name=HRL003 --cmd='python Run_Robosuite_PPO.py --run_name="HRL003" --hierarchical=1 --env="SawyerPickPlace"'

python cluster_run.py --partition=learnfair --name=HRL004 --cmd='python Run_Robosuite_PPO.py --run_name="HRL004" --hierarchical=1 --env="SawyerNutAssembly"'

python cluster_run.py --partition=learnfair --name=HRL005 --cmd='python Run_Robosuite_PPO.py --run_name="HRL005" --hierarchical=1 --env="BaxterLift"'

python cluster_run.py --partition=learnfair --name=HRL006 --cmd='python Run_Robosuite_PPO.py --run_name="HRL006" --hierarchical=1 --env="BaxterPegInHole"'

python cluster_run.py --partition=learnfair --name=HRL007 --cmd='python Run_Robosuite_PPO.py --run_name="HRL007" --hierarchical=1 --env="SawyerPickPlaceBread"'

python cluster_run.py --partition=learnfair --name=HRL008 --cmd='python Run_Robosuite_PPO.py --run_name="HRL008" --hierarchical=1 --env="SawyerPickPlaceCan"'

python cluster_run.py --partition=learnfair --name=HRL009 --cmd='python Run_Robosuite_PPO.py --run_name="HRL009" --hierarchical=1 --env="SawyerPickPlaceCereal"'

python cluster_run.py --partition=learnfair --name=HRL010 --cmd='python Run_Robosuite_PPO.py --run_name="HRL010" --hierarchical=1 --env="SawyerPickPlaceMilk"'

python cluster_run.py --partition=learnfair --name=HRL011 --cmd='python Run_Robosuite_PPO.py --run_name="HRL012" --hierarchical=1 --env="SawyerNutAssemblyRound"'

python cluster_run.py --partition=learnfair --name=HRL012 --cmd='python Run_Robosuite_PPO.py --run_name="HRL013" --hierarchical=1 --env="SawyerNutAssemblySquare"'

#####################################################


# Running Hierarchical PPO on all environments. 
# trial 
python Run_Robosuite_PPO.py --run_name="trial" --hierarchical=1 --env="SawyerLift"

python Run_Robosuite_PPO.py --run_name="HRL001" --hierarchical=1 --env="SawyerLift"

python Run_Robosuite_PPO.py --run_name="HRL002" --hierarchical=1 --env="SawyerStack"

python Run_Robosuite_PPO.py --run_name="HRL003" --hierarchical=1 --env="SawyerPickPlace"

# 
# Run without hierarchy for comparison
python Run_Robosuite_PPO.py --run_name="RL001" --hierarchical=0 --env="SawyerLift"

python Run_Robosuite_PPO.py --run_name="RL002" --hierarchical=0 --env="SawyerStack"

python Run_Robosuite_PPO.py --run_name="RL003" --hierarchical=0 --env="SawyerPickPlace"

python Run_Robosuite_PPO.py --run_name="HRL004" --hierarchical=1 --env="SawyerNutAssembly"

python Run_Robosuite_PPO.py --run_name="HRL005" --hierarchical=1 --env="BaxterLift"

python Run_Robosuite_PPO.py --run_name="HRL006" --hierarchical=1 --env="BaxterPegInHole"

python Run_Robosuite_PPO.py --run_name="HRL007" --hierarchical=1 --env="SawyerPickPlaceBread"

python Run_Robosuite_PPO.py --run_name="HRL008" --hierarchical=1 --env="SawyerPickPlaceCan"

python Run_Robosuite_PPO.py --run_name="HRL009" --hierarchical=1 --env="SawyerPickPlaceCereal"

python Run_Robosuite_PPO.py --run_name="HRL010" --hierarchical=1 --env="SawyerPickPlaceMilk"

python Run_Robosuite_PPO.py --run_name="HRL012" --hierarchical=1 --env="SawyerNutAssemblyRound"

python Run_Robosuite_PPO.py --run_name="HRL013" --hierarchical=1 --env="SawyerNutAssemblySquare"

# Trial
python Run_Robosuite_PPO.py --run_name="trailzz" --hierarchical=1 --env="SawyerNutAssembly" --data=Roboturk
# 
python Run_Robosuite_PPO.py --run_name="trailzz" --hierarchical=0 --env="SawyerNutAssembly" --data=Roboturk
#
# Trial with model
# python Run_Robosuite_PPO.py --run_name="trail_with_model" --hierarchical=1 --env="SawyerNutAssembly" --data=Roboturk --lowlevel_policy_model="~/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340"

python Run_Robosuite_PPO.py --run_name="trail_with_model" --hierarchical=1 --env="SawyerNutAssembly" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_001/saved_models/Model_epoch105"

# Actually run on easy tasks
python Run_Robosuite_PPO.py --run_name="HRL_100" --hierarchical=1 --env="SawyerLift" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_001/saved_models/Model_epoch105" --target_kl=0.03

python Run_Robosuite_PPO.py --run_name="HRL_101" --hierarchical=1 --env="SawyerLift" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_001/saved_models/Model_epoch105" --target_kl=0.04

CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_102" --hierarchical=1 --env="SawyerLift" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_001/saved_models/Model_epoch105" --target_kl=0.05

# CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_101" --hierarchical=1 --env="SawyerStack" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_001/saved_models/Model_epoch105"

# python Run_Robosuite_PPO.py --run_name="HRL_102" --hierarchical=1 --env="SawyerLift" --data=Roboturk

# CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_103" --hierarchical=1 --env="SawyerStack" --data=Roboturk

# Contrasting run
CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="RL_101" --hierarchical=0 --env="SawyerLift"

# 
python Run_Robosuite_PPO.py --run_name="HRL_106" --hierarchical=1 --env="SawyerLift" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=2.

python Run_Robosuite_PPO.py --run_name="HRL_107" --hierarchical=1 --env="SawyerLift" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=5.

CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_108" --hierarchical=1 --env="SawyerLift" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=10.

CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_109" --hierarchical=1 --env="SawyerLift" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=1.


#################################################################

# Debug
python Run_Robosuite_PPO.py --run_name="HRL_debug" --hierarchical=1 --env="SawyerLift" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=1.

#
# Run with.. hierachy, loading model
python Run_Robosuite_PPO.py --run_name="HRL_201" --hierarchical=1 --env="SawyerLift" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=1.

python Run_Robosuite_PPO.py --run_name="HRL_202" --hierarchical=1 --env="SawyerStack" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=1.

CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_203" --hierarchical=1 --env="SawyerPickPlaceBread" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=1.

CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_204" --hierarchical=1 --env="SawyerPickPlaceCan" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=1.

python Run_Robosuite_PPO.py --run_name="HRL_205" --hierarchical=1 --env="SawyerPickPlaceCereal" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=1.

python Run_Robosuite_PPO.py --run_name="HRL_206" --hierarchical=1 --env="SawyerPickPlaceMilk" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=1.

CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_207" --hierarchical=1 --env="SawyerNutAssemblyRound" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=1.

CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_208" --hierarchical=1 --env="SawyerNutAssemblySquare" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=1.

# Run without hierarchy
CUDA_VISIBLE_DEVICES=0 python Run_Robosuite_PPO.py --run_name="HRL_301" --hierarchical=0 --env="SawyerLift" --data=Roboturk --action_scaling=1.

CUDA_VISIBLE_DEVICES=0 python Run_Robosuite_PPO.py --run_name="HRL_302" --hierarchical=0 --env="SawyerStack" --data=Roboturk --action_scaling=1.

# CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_303" --hierarchical=0 --env="SawyerPickPlaceBread" --data=Roboturk --action_scaling=1.

# CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_304" --hierarchical=0 --env="SawyerPickPlaceCan" --data=Roboturk --action_scaling=1.

# CUDA_VISIBLE_DEVICES=0 python Run_Robosuite_PPO.py --run_name="HRL_305" --hierarchical=0 --env="SawyerPickPlaceCereal" --data=Roboturk --action_scaling=1.

# CUDA_VISIBLE_DEVICES=0 python Run_Robosuite_PPO.py --run_name="HRL_306" --hierarchical=0 --env="SawyerPickPlaceMilk" --data=Roboturk --action_scaling=1.

# CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_307" --hierarchical=0 --env="SawyerNutAssemblyRound" --data=Roboturk --action_scaling=1.

# CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_308" --hierarchical=0 --env="SawyerNutAssemblySquare" --data=Roboturk --action_scaling=1.


# Run with hierarchy, no loading model
python Run_Robosuite_PPO.py --run_name="HRL_211" --hierarchical=1 --env="SawyerLift" --data=Roboturk --action_scaling=1.

python Run_Robosuite_PPO.py --run_name="HRL_212" --hierarchical=1 --env="SawyerStack" --data=Roboturk --action_scaling=1.

# Now running on Door and Wiping tasks
# Run without hierarchy
python Run_Robosuite_PPO.py --run_name="HRL_303" --hierarchical=0 --env="Door" --data=Roboturk

python Run_Robosuite_PPO.py --run_name="HRL_304" --hierarchical=0 --env="Wipe" --data=Roboturk


# Now running on Door and Wiping tasks
# Run with.. hierachy, loading model
python Run_Robosuite_PPO.py --run_name="HRL_221" --hierarchical=1 --env="Door" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=1.

python Run_Robosuite_PPO.py --run_name="HRL_222" --hierarchical=1 --env="Wipe" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=1.


# Evaluate various z's... 
python Run_Robosuite_PPO.py --run_name="HRL_evalMIMEwipes" --hierarchical=1 --env="Wipe" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=1.

# 
python Run_Robosuite_PPO.py --run_name="HRL_evalMIMEwipes2" --hierarchical=1 --env="Wipe" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --evaluate_translated_zs=1 --translated_z_file="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/Wiping_Trajectories_TranslatedZs_RMIME_160to165.npy" --action_scaling=1.


# Zero shot evaluation across different action scalings.
python Run_Robosuite_PPO.py --run_name="HRL_evalMIMEwipes2" --hierarchical=1 --env="Wipe" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --evaluate_translated_zs=1 --translated_z_file="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/Wiping_Trajectories_TranslatedZs_RMIME_160to165.npy" --action_scaling=1.

# python Run_Robosuite_PPO.py --run_name="HRL_evalMIMEwipes2" --hierarchical=1 --env="Wipe" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --evaluate_translated_zs=1 --translated_z_file="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/Wiping_Trajectories_TranslatedZs_RMIME_160to165.npy" --action_scaling=2.

# python Run_Robosuite_PPO.py --run_name="HRL_evalMIMEwipes2" --hierarchical=1 --env="Wipe" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --evaluate_translated_zs=1 --translated_z_file="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/Wiping_Trajectories_TranslatedZs_RMIME_160to165.npy" --action_scaling=5.

# python Run_Robosuite_PPO.py --run_name="HRL_evalMIMEwipes2" --hierarchical=1 --env="Wipe" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --evaluate_translated_zs=1 --translated_z_file="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/Wiping_Trajectories_TranslatedZs_RMIME_160to165.npy" --action_scaling=10.


# Rerun HRL with new rollout timesteps on the 4 envs
python Run_Robosuite_PPO.py --run_name="HRL_231" --hierarchical=1 --env="Door" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=1.

python Run_Robosuite_PPO.py --run_name="HRL_232" --hierarchical=1 --env="Wipe" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=1.

CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_233" --hierarchical=1 --env="SawyerLift" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=1.

CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_234" --hierarchical=1 --env="SawyerStack" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=1.

# 
# Rerun HRL with new rollout timesteps on the 4 envs
python Run_Robosuite_PPO.py --run_name="HRL_241" --hierarchical=1 --env="Door" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=1.

python Run_Robosuite_PPO.py --run_name="HRL_242" --hierarchical=1 --env="Wipe" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=1.

CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_243" --hierarchical=1 --env="SawyerLift" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=1.

CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_244" --hierarchical=1 --env="SawyerStack" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=1.

CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_trial" --hierarchical=1 --env="SawyerStack" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=1.


# Run things with way more epochs
# 
# Rerun HRL with new rollout timesteps on the 4 envs
CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_251" --hierarchical=1 --env="Door" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=1. --epochs=500

CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_252" --hierarchical=1 --env="Wipe" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=1. --epochs=500

CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_253" --hierarchical=1 --env="SawyerLift" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=1. --epochs=500

CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_254" --hierarchical=1 --env="SawyerStack" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=1. --epochs=500

# # Rerun HRL with 4000 steps per epoch
CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_261" --hierarchical=1 --env="Door" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=1. --epochs=500

CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_262" --hierarchical=1 --env="Wipe" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=1. --epochs=500

CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_263" --hierarchical=1 --env="SawyerLift" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=1. --epochs=500

CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_264" --hierarchical=1 --env="SawyerStack" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=1. --epochs=500

# Debugging step size in Robosuite 1.2.1
CUDA_VISIBLE_DEVICES=0 python Run_Robosuite_PPO.py --run_name="HRL_271" --hierarchical=1 --env="Door" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=2. --epochs=500

CUDA_VISIBLE_DEVICES=0 python Run_Robosuite_PPO.py --run_name="HRL_272" --hierarchical=1 --env="Door" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=5. --epochs=500

CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_273" --hierarchical=1 --env="Door" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=10. --epochs=500

CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_274" --hierarchical=1 --env="Door" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=20. --epochs=500

CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_275" --hierarchical=1 --env="Door" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=50. --epochs=500

# # RUNNING WITH ACTION SCALING ON VERDI
# CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_283" --hierarchical=1 --env="Wipe" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=10. --epochs=500

# CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_284" --hierarchical=1 --env="Wipe" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=20. --epochs=500

# CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_285" --hierarchical=1 --env="Wipe" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=50. --epochs=500

#Running on Wipe with increased step size.
CUDA_VISIBLE_DEVICES=0 python Run_Robosuite_PPO.py --run_name="HRL_281" --hierarchical=1 --env="Wipe" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=2. --epochs=500

CUDA_VISIBLE_DEVICES=0 python Run_Robosuite_PPO.py --run_name="HRL_282" --hierarchical=1 --env="Wipe" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=5. --epochs=500

CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_283" --hierarchical=1 --env="Wipe" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=10. --epochs=500

CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_284" --hierarchical=1 --env="Wipe" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=20. --epochs=500

CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_285" --hierarchical=1 --env="Wipe" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=50. --epochs=500

# Dbug on verdi
CUDA_VISIBLE_DEVICES=0 python Run_Robosuite_PPO.py --run_name="HRL_debugverdi" --hierarchical=1 --env="Wipe" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=2. --epochs=500

# Run with increased clip
#
CUDA_VISIBLE_DEVICES=0 python Run_Robosuite_PPO.py --run_name="HRL_291" --hierarchical=1 --env="Wipe" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=2. --epochs=500  --target_kl=0.05

CUDA_VISIBLE_DEVICES=0 python Run_Robosuite_PPO.py --run_name="HRL_292" --hierarchical=1 --env="Wipe" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=5. --epochs=500 --target_kl=0.05

CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_293" --hierarchical=1 --env="Door" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=20. --epochs=500 --target_kl=0.05

CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_294" --hierarchical=1 --env="Door" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=50. --epochs=500 --target_kl=0.05


##################################
# Baxter Left Hand Lift
python Run_Robosuite_PPO.py --run_name="HRL_baxtrial" --hierarchical=0 --env="BaxterLeftHandLift"

python Run_Robosuite_PPO.py --run_name="HRL_baxtrial" --hierarchical=0 --env="BaxterRightHandLift"

python Run_Robosuite_PPO.py --run_name="RL_baxstack_onehand_l" --hierarchical=0 --env="BaxterLeftHandStack"

python Run_Robosuite_PPO.py --run_name="RL_baxstack_onehand_r" --hierarchical=0 --env="BaxterRightHandStack"

#################################
# Run Hierarchical PPO while loading Baxter model

CUDA_VISIBLE_DEVICES=0 python Run_Robosuite_PPO.py --run_name="HRL_Bax_001" --hierarchical=1 --env="BaxterLeftHandLift" --data=MIME --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/MJ_116/saved_models/Model_epoch500" --action_scaling=1.0 --epochs=500

CUDA_VISIBLE_DEVICES=0 python Run_Robosuite_PPO.py --run_name="HRL_Bax_002" --hierarchical=1 --env="BaxterRightHandLift" --data=MIME --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/MJ_116/saved_models/Model_epoch500" --action_scaling=1.0 --epochs=500

CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_Bax_003" --hierarchical=1 --env="BaxterLeftHandStack" --data=MIME --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/MJ_116/saved_models/Model_epoch500" --action_scaling=1.0 --epochs=500

CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_Bax_004" --hierarchical=1 --env="BaxterRightHandStack" --data=MIME --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/MJ_116/saved_models/Model_epoch500" --action_scaling=1.0 --epochs=500

# Rerun with diff init 
CUDA_VISIBLE_DEVICES=0 python Run_Robosuite_PPO.py --run_name="HRL_Bax_011" --hierarchical=1 --env="BaxterLeftHandLift" --data=MIME --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/MJ_116/saved_models/Model_epoch500" --action_scaling=1.0 --epochs=500

CUDA_VISIBLE_DEVICES=0 python Run_Robosuite_PPO.py --run_name="HRL_Bax_012" --hierarchical=1 --env="BaxterRightHandLift" --data=MIME --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/MJ_116/saved_models/Model_epoch500" --action_scaling=1.0 --epochs=500

CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_Bax_013" --hierarchical=1 --env="BaxterLeftHandStack" --data=MIME --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/MJ_116/saved_models/Model_epoch500" --action_scaling=1.0 --epochs=500

CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_Bax_014" --hierarchical=1 --env="BaxterRightHandStack" --data=MIME --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/MJ_116/saved_models/Model_epoch500" --action_scaling=1.0 --epochs=500

# Debug
CUDA_VISIBLE_DEVICES=0 python Run_Robosuite_PPO.py --run_name="DebugBax" --hierarchical=1 --env="BaxterLeftHandLift" --data=MIME --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/MJ_116/saved_models/Model_epoch500" --action_scaling=1.0 --epochs=1

# Rerun flat with diff init
CUDA_VISIBLE_DEVICES=0 python Run_Robosuite_PPO.py --run_name="RL_Bax_001" --hierarchical=0 --env="BaxterLeftHandLift"

CUDA_VISIBLE_DEVICES=0 python Run_Robosuite_PPO.py --run_name="RL_Bax_002" --hierarchical=0 --env="BaxterRightHandLift"

CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="RL_Bax_003" --hierarchical=0 --env="BaxterLeftHandStack"

CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="RL_Bax_004" --hierarchical=0 --env="BaxterRightHandStack"

# 
# Rerun with diff init and fixed left right hands
CUDA_VISIBLE_DEVICES=0 python Run_Robosuite_PPO.py --run_name="HRL_Bax_021" --hierarchical=1 --env="BaxterLeftHandLift" --data=MIME --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/MJ_116/saved_models/Model_epoch500" --action_scaling=1.0 --epochs=500

CUDA_VISIBLE_DEVICES=0 python Run_Robosuite_PPO.py --run_name="HRL_Bax_022" --hierarchical=1 --env="BaxterRightHandLift" --data=MIME --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/MJ_116/saved_models/Model_epoch500" --action_scaling=1.0 --epochs=500

CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_Bax_023" --hierarchical=1 --env="BaxterLeftHandStack" --data=MIME --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/MJ_116/saved_models/Model_epoch500" --action_scaling=1.0 --epochs=500

CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_Bax_024" --hierarchical=1 --env="BaxterRightHandStack" --data=MIME --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/MJ_116/saved_models/Model_epoch500" --action_scaling=1.0 --epochs=500

# trial 
CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_Bax_trail" --hierarchical=1 --env="BaxterRightHandStack" --data=MIME --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/MJ_116/saved_models/Model_epoch500" --action_scaling=1.0 --epochs=500

# Rerun with diff init and fixed left right hands
CUDA_VISIBLE_DEVICES=0 python Run_Robosuite_PPO.py --run_name="RL_Bax_021" --hierarchical=0 --env="BaxterLeftHandLift"

CUDA_VISIBLE_DEVICES=0 python Run_Robosuite_PPO.py --run_name="RL_Bax_022" --hierarchical=0 --env="BaxterRightHandLift"

CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="RL_Bax_023" --hierarchical=0 --env="BaxterLeftHandStack"

CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="RL_Bax_024" --hierarchical=0 --env="BaxterRightHandStack"

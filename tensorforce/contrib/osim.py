# Copyright 2018 Tensorforce Team. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

from osim.env import L2RunEnv, Arm2DEnv, ProstheticsEnv

from tensorforce.environments import Environment

class OpenSim(Environment):
	"""
	Reinforcement learning with musculoskeletal models in OpenSim Integration:
	http://osim-rl.stanford.edu/
	"""

	def __init__(self,env_id,visualize=False):
		"""
		Initialize OpenSimulator environment.

		Args:
			visualize: render enviroment
			env: environment id to use ([0:Arm2DEnv, 1:L2RunEnv, 2:ProstheticsEnv])
		"""	
		envs = [Arm2DEnv,L2RunEnv,ProstheticsEnv]
		self.env = envs[env_id](visualize=visualize)

		self.state_shape = len(self.env.reset())
		self.num_actions = len(self.env.action_space.sample())
	
	def __str__(self):
		return 'OpenSim'

	def close(self):
		self.env.close()

	def reset(self):
		obs = self.env.reset()
		return obs

	def execute(self, action):
		observation, reward, done, info = self.env.step(action)
		return (observation,done,reward)

	@property
	def states(self):
		return dict(shape=self.state_shape, type='float')

	@property
	def actions(self):
		return dict(shape=self.num_actions, type='float')
import numpy as np
import matplotlib.pyplot as plt

import naplib as nl

nCh = 20 # number of recording channels in the responses
fs = 100 # sampling rate of the response data
audio_fs = 16000 # sampling rate of the audio stimuli
trial_lengths = [5.0, 6.7, 5.8] # length of each trial (in seconds)
tone_frequencies = [2, 5, 8] # frequency (Hz) of each trial's stimulus tone

trial_responses = [np.random.normal(size=(int(L*fs), nCh)) for L in trial_lengths]
trial_stimuli = [np.sin(2 * np.pi * freq * np.linspace(0, L, int(L*audio_fs))) for freq, L in zip(tone_frequencies, trial_lengths)]

data_dict = {'name': ['trial-1','trial-2','trial-3'],
             'soundf': [audio_fs, audio_fs, audio_fs],
             'sound': trial_stimuli,
             'dataf': [fs, fs, fs],
             'resp': trial_responses
             }

data = nl.Data(data_dict)


# We can plot the stimuli or responses easily

fig, axes = plt.subplots(2,1, figsize=(8,3))
axes[0].set_title('trial-1')
axes[0].plot(data[0]['sound'])
axes[1].plot(data[0]['resp'])
plt.tight_layout()
plt.show()

fig, axes = plt.subplots(2,1, figsize=(8,3))
axes[0].set_title('trial-2')
axes[0].plot(data[1]['sound'])
axes[1].plot(data[1]['resp'])
plt.tight_layout()
plt.show()

fig, axes = plt.subplots(2,1, figsize=(8,3))
axes[0].set_title('trial-2')
axes[0].plot(data[2]['sound'])
axes[1].plot(data[2]['resp'])
plt.tight_layout()
plt.show()

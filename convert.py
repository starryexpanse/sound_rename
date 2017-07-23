import subprocess
import os

mappings = {
	't_Sounds': (
		('twindstm_1.mp2', 'T_wind_ambience.wav'),
	),
}

for k, tuples in mappings.items():
	for v in tuples:
		infile = os.path.join(k, v[0])
		args = ['ffmpeg', '-i', infile]
		if len(v) > 2:
			args += ['-ss', str(v[2]), '-to', str(v[3]), '-c', 'copy']
		outfile = os.path.join(k + '_renamed', v[1])
		args += [outfile]
		p = subprocess.Popen(args, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
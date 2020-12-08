python -m experiments.unet_experiment datasets/membrane.pickle -e 500 -b 5 -p 1 -w 4 -mp 1 -f memb1 -s "[[0],[1,3,2,2,3],[0,0,0,1],[0,2,2],[0,0,0,0],[0,0,0,0],[0,0,0],[4,1,4,2],[4,5,6,0],[],[],[0,0,0,2],[0,0,0]]" >> memb1.log
python -m experiments.unet_experiment datasets/membrane.pickle -e 500 -b 5 -p 1 -w 4 -mp 1 -f memb2 -s "[[0],[0,1,0,3,3],[0,1],[0,1,1],[0,0,0,0,0,0],[0,0],[0],[3,4,3,2,3,3],[3,6,5,5,5,2],[],[],[2,0,2,2,1,2],[0]]" >> memb2.log
python -m experiments.unet_experiment datasets/membrane.pickle -e 500 -b 5 -p 1 -w 4 -mp 1 -f memb3 -s "[[0],[2,2],[0,1],[2],[0,0],[0,0],[0],[4,4],[4,5],[],[],[2,2],[0]]" >> memb3.log
python -m experiments.unet_experiment datasets/membrane.pickle -e 500 -b 5 -p 1 -w 4 -mp 1 -f memb4 -s "[[0],[0,2],[1],[1],[0,0,0],[0],[],[3,4,4],[5,6,5],[],[],[0,2,0],[]]" >> memb4.log
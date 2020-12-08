python -m experiments.unet_experiment datasets/bsds500gray.pickle -e 500 -b 5 -p 1 -w 4 -mp 1 -f gray1 -s "[[0],[1,0,1,1,0,1,3],[1],[2],[0,0,0],[0],[0,0,0,0,0],[2,4,0],[4,2,2],[],[],[2,0,1],[0,0,0,0,0]]"
python -m experiments.unet_experiment datasets/bsds500gray.pickle -e 500 -b 5 -p 1 -w 4 -mp 1 -f gray2 -s "[[0],[0,2,2,0,2,1,3],[0,0,0,1],[1],[0,0,0,0,0,0,0],[0,0,0,0],[0],[1,0,1,2,1,1,2],[2,6,5,6,6,0,2],[],[],[1,2,0,2,2,1,2],[0]]"
python -m experiments.unet_experiment datasets/bsds500gray.pickle -e 500 -b 5 -p 1 -w 4 -mp 1 -f gray3 -s "[[0],[1,1,1,2],[1],[0,1,0,1,0,1,0,1,0,0,0,1,0,0,1,2,0,1,2,0,1,2,2],[0,0,0,0,0,0,0,0,0],[0],[0,0,0,0,0,0,0],[1,3,0,1,2,3,3,2,1],[1,0,0,3,4,5,5,6,3],[],[],[1,0,0,0,2,0,2,0,2],[0,0,0,0,0,0,0]]"
python -m experiments.unet_experiment datasets/bsds500gray.pickle -e 500 -b 5 -p 1 -w 4 -mp 1 -f gray4 -s "[[0],[0,3,1,2,3],[0,0,1],[0,1,2],[0,0,0,0,0],[0,0,0],[0,0],[4,2,4,0,0],[6,3,0,5,5],[],[],[1,1,0,0,2],[0,0]]"
python -m experiments.unet_experiment datasets/bsds500gray.pickle -e 500 -b 5 -p 1 -w 4 -mp 1 -f gray5 -s "[[0],[1,0,1,3,2],[0,1],[2],[0,0,0],[0,0],[0,0,0],[3,2,1],[4,1,4],[],[],[0,0,1],[0,0,0]]"
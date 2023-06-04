# first build
@2nd build
3rd build


git branch -m main master
git fetch origin
git branch -u origin/master master
git remote set-head origin -a
4th commit
5th commit
6th commit
7th commit
8 th commoit
9th commit
10th 11


New token created
Key:
1a43482a-26c1-43a8-b956-dcb78b59c9f8
Secret:
8nGhyEUMEz30
To configure relay CLI, run the following command:
relay login -k 1a43482a-26c1-43a8-b956-dcb78b59c9f8 -s 8nGhyEUMEz30
To use credentials as an environment variables:
            
export RELAY_KEY=1a43482a-26c1-43a8-b956-dcb78b59c9f8
export RELAY_SECRET=8nGhyEUMEz30

            
To create Kubernetes Secret:
              
kubectl create secret generic whr-credentials \
    --from-literal=key=1a43482a-26c1-43a8-b956-dcb78b59c9f8 \
    --from-literal=secret=8nGhyEUMEz30

            
Please note that once you close this window you will not be able to see the token secret again as it is now encrypted. If you lose your secret, just generate a new token.

12
13
import sys
import shlex
import subprocess as sp


import sys
import shlex 
import subprocess as sp

def launchModelStep1 (filepath, phenotype = "pheno_data.txt"):

    print ("****** Begin JOB:' " + str(filepath) + "'")

    #for path in filepath :
    print ('*************************************')
    print ('This is the working path entered from the user:', str(filepath))

    ## Create system command

    # cmd = "sbatch -p standard -o " + filepath + "/model_setup_step1.out ./bin/model_setup_step1.sh  " + filepath + " " +   str(phenotype)

    cmd = "srun --partition=bioinfo --cpus-per-task=8 -o  " + filepath + "/model_setup_step1.out ./bin/model_setup_step1.sh  " + filepath +  "  " + str(phenotype)
    print (cmd)
    sp.call(cmd,  shell=True)
    print ("Launching model setup step 1:" +  cmd)
    print ("Check the job status with command: squeue ")


def launchModelStep2 (filepath):

    print ("****** Begin JOB:' " + str(filepath) + "'")

    #for path in filepath :
    print ('*************************************')
    print ('This is the working path entered from the user:', str(filepath))

    ## Create system command
    ## ('sbatch -p standard -o '+path+'/model_setup_step2.out ./bin/model_setup_step2.sh',path))
    cmd = "srun --partition=bioinfo --cpus-per-task=8 -o  " + filepath + "/model_setup_step2.out ./bin/model_setup_step2.sh  " + filepath
    print (cmd)
    sp.call(cmd,  shell=True)

    print ("Launching model setup step 2:" +  cmd)
    print ("Check the job status with command: squeue ")


def launchHeritability (filepath):

    print ("****** Begin JOB:' " + str(filepath) + "'")
    #for path in filepath :
    print ('*************************************')
    print ('This is the working path entered from the user:', str(filepath))

    ## Create system command

    # cmd = 'sbatch -p standard -o '+path+'/sbatch_logs/gcta.out ./bin/run_gcta.sh',path))
    cmd = "srun --partition=bioinfo --cpus-per-task=8 -o  " + filepath + "/sbatch_logs/gcta.out  ./bin/run_gcta.sh  " + filepath
    print (cmd)
    sp.call(cmd,  shell=True)
    print ("Launching launchHeritability step 1 of 3:" + cmd)
    print ("Check the job status with command: squeue ")


def genoCommondVarAnalysis (filepath):

    print ("****** Begin JOB:' " + str(filepath) + "'")
    #for path in filepath :
    print ('*************************************')
    print ('This is the working path entered from the user:', str(filepath))

    ## Create system command

    # cmd = 'sbatch -p standard -o '+path+'/sbatch_logs/gcta.out ./bin/run_gcta.sh',path))
    cmd = "place holder"
    print (cmd)
    sp.call(cmd,  shell=True)
    print ("Launching genotype common variant analysis  step 2 of 3:" + cmd)
    print ("Check the job status with command: squeue ")


def imputeCommondVarAnalysis (filepath):

    print ("****** Begin JOB:' " + str(filepath) + "'")
    #for path in filepath :
    print ('*************************************')
    print ('This is the working path entered from the user:', str(filepath))

    ## Create system command

    # cmd = 'sbatch -p standard -o '+path+'/sbatch_logs/gcta.out ./bin/run_gcta.sh',path))
    cmd = "place holder"
    print (cmd)
    sp.call(cmd,  shell=True)
    print ("Launching impute common variant analysis  step 3 of 3:" + cmd)
    print ("Check the job status with command: squeue ")

# Constants (User configurable)

APP_NAME = 'DistributedFIJI'                # Used to generate derivative names unique to the application.

# DOCKER REGISTRY INFORMATION:
DOCKERHUB_TAG = 'bethcimini/distributed-fiji:latest'

# AWS GENERAL SETTINGS:
AWS_REGION = 'us-east-1'
AWS_PROFILE = 'default'                 # The same profile used by your AWS CLI installation
SSH_KEY_NAME = 'your-key-file.pem'      # Expected to be in ~/.ssh
AWS_BUCKET = 'your-bucket-name'

# EC2 AND ECS INFORMATION:
ECS_CLUSTER = 'default'
CLUSTER_MACHINES = 3
TASKS_PER_MACHINE = 1
EBS_VOL_SIZE = 30                       # In GB.  Minimum allowed is 22.  Docker will get this - 2 GB

# DOCKER INSTANCE RUNNING ENVIRONMENT:
MEMORY = 4096                           # Memory assigned to the docker container in MB
SCRIPT_DOWNLOAD_URL = 'https://some/url/with/a/script.y'

# SQS QUEUE INFORMATION:
SQS_QUEUE_NAME = APP_NAME + 'Queue'
SQS_MESSAGE_VISIBILITY = 1*60           # Timeout (secs) for messages in flight (average time to be processed)
SQS_DEAD_LETTER_QUEUE = 'arn:aws:sqs:some-region:111111100000:DeadMessages'

# LOG GROUP INFORMATION:
LOG_GROUP_NAME = APP_NAME 

# REDUNDANCY CHECKS
EXPECTED_NUMBER_FILES = 7    #What is the number of files that trigger that a job completed successfully?
MIN_FILE_SIZE_BYTES = 1      #What is the minimal number of bytes an object should be to "count"?

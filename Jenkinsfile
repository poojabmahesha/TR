#!groovy

library identifier: 'tat-jenkins-pipeline-lib@master', retriever: modernSCM(
        github(
                apiUri: 'https://github.ford.com/api/v3', 
                credentialsId: 'fnvtat-github-token', 
                repoOwner: 'TAT', 
                repository: 'jenkins-pipeline-lib'
        )
)

basePythonProject()

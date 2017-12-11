#!/usr/bin/env groovy

pipeline {
  agent { label 'docker' }
  
  options {
    timeout(time: 1, unit: 'HOURS')
    buildDiscarder(logRotator(numToKeepStr: '5'))
  }
  
  triggers {
    cron('@daily')
  }
  
  stages {
    stage('build'){
      steps {
        container('docker-runner'){
          sh 'sh ./jenkins-build.sh'
          sh 'ls -al'
          archiveArtifacts 'repo/**'
          archiveArtifacts 'ca_CMS-TTS-CA.repo'
        }
      }
    }
    
    stage('result'){
      steps {
        script {
          currentBuild.result = 'SUCCESS'
        }
      }
    }
  }
  
  post {
    failure {
      slackSend color: 'danger', message: "${env.JOB_NAME} - #${env.BUILD_NUMBER} Failure (<${env.BUILD_URL}|Open>)"
    }
    
    changed {
      script{
        if('SUCCESS'.equals(currentBuild.result)) {
          slackSend color: 'good', message: "${env.JOB_NAME} - #${env.BUILD_NUMBER} Back to normal (<${env.BUILD_URL}|Open>)"
        }
      }
    }
  }
}

#!groovy

properties([
  buildDiscarder(logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '', daysToKeepStr: '', numToKeepStr: '5')),
    pipelineTriggers([cron('@daily')])
])

stage('prepare'){
  node('generic'){
    git branch: 'master', url: 'https://github.com/cnaf-mw-devel/ca_CMS-TTS-CA.git'
    stash include: './*', name: 'code'
  }
}

stage('build'){
  node('docker') {
    unstash 'code'
    sh 'sh ./jenkins-build.sh'
    sh 'ls -al'
    archiveArtifacts 'repo/**'
    archiveArtifacts 'ca_CMS-TTS-CA.repo'
  }
}

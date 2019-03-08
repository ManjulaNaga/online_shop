node {
  stage('SCM') {
    git 'https://github.com/ManjulaNaga/online_shop.git'
  }
  stage('SonarQube analysis 1') {
    sh 'mvn clean package sonar:sonar'
  }
  stage('SonarQube analysis') {
    // requires SonarQube Scanner 2.8+
    def scannerHome = tool 'sonarqube';
    withSonarQubeEnv('sonarqube') {
      sh "${scannerHome}/bin/sonar-scanner"
    }
  }
}

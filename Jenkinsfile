pipeline{
  agent any
  stages{
    stage('setup'){
      steps{
        sh "sudo apt install python3-venv -y"
        sh "python3 -m venv venv"
        sh ". venv/bin/activate"
        sh "pip3 install -r requirements.txt"
      }
    }
    stage('run python app'){
      steps{
        sh "python3 app.py"
      }
    }
  }
}

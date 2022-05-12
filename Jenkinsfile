pipeline {
   agent {
        docker{
            image 'image 'mcr.microsoft.com/playwright:v1.21.0-focal'
        }
   }
   stages {
      stage('install playwright') {
         steps {
            sh '''
                pip install playwright
                playwright install
            '''
         }
      }

      stage('help'){
        steps{
            sh 'playwright --help'
        }
      }

      stage('test'){
        steps{
            sh '''
                npx playwright test --list
                npx playwright test
            '''
        }
      }

    }

   }


   

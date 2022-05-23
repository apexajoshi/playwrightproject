pipeline {
   agent {
        docker{
            image  'mcr.microsoft.com/playwright:v1.21.0-focal'
        }
   }
   stages {
      stage('install playwright') {
         steps {
            sh '''
                npm i -D@plawright/test
                npx playwright install
            '''
         }
      }

     

    }

   }


   

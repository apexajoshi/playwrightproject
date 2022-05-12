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
                pip install playwright
                playwright install --with-deps
            '''
         }
      }

     

    }

   }


   

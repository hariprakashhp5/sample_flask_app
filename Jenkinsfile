def IMAGE_NAME="sample-flask-app"
def IMAGE_TAG="latest"

node {

    stage('Initialize'){
        def dockerHome = tool 'myDocker'
        env.PATH = "${dockerHome}/bin:${env.PATH}"
    }

#    stage('Checkout') {
#        checkout scm
#    }

    stage("Image Prune"){
        imagePrune(IMAGE_NAME)
    }

    stage('Image Build'){
        imageBuild(IMAGE_NAME, IMAGE_TAG)
    }


    stage('Run App'){
        sh "docker-compose -f docker-compose.yml up -d --build"
        echo "Application started Successfully!"
    }

}

def imagePrune(containerName){
    try {
        sh "docker image prune -f"
        sh "docker stop $containerName"
    } catch(error){}
}

def imageBuild(imageName, tag){
    sh "docker build -t $imageName:$tag  -t $imageName --pull --no-cache ."
    echo "Image build complete"
}
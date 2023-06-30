import os
import docker
from multiprocessing import Pool

DOCKERFILES_DIRECTORY = "/home/crazypikachu/Desktop/development/DockerImages/dockerfiles/submitty/"  # Replace with the path to your directory containing Dockerfiles
dockefile_ignore =[ "3.6","3.5","3.8","2.7","4.0","5.0","6.0","7","8","database_client"]
def build_dockerfile(dockerfile):
    directory = os.path.dirname(dockerfile)
    image_tag = os.path.basename(directory)

    client = docker.from_env()
    if(image_tag in dockefile_ignore):
        return
    
    # print(type(image_tag))
    try:
        image, _ = client.images.build(path=directory, dockerfile=dockerfile, tag=image_tag)
        print(f"Build successful: {image.tags}")
    except docker.errors.BuildError as e:
        print(f"Build failed for {dockerfile}: {e}")
    except docker.errors.APIError as e:
        print(f"Docker API error occurred while building {dockerfile}: {e}")


def find_dockerfiles(directory):
    dockerfiles=[]
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == "Dockerfile":
                # print(os.path.join(root,file))
                dockerfiles.append(os.path.join(root,file))

    return dockerfiles


if __name__ == "__main__":
    dockerfiles=find_dockerfiles(DOCKERFILES_DIRECTORY)
    num_processes = min(len(dockerfiles), os.cpu_count())

    with Pool(processes=num_processes) as pool:
        pool.map(build_dockerfile, dockerfiles)

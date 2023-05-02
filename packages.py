import yaml
import subprocess

packages = []

with open("packages.yml", "r") as stream:
    try:
        yaml_stream = yaml.safe_load(stream)
        packages = yaml_stream['packages']
    except yaml.YAMLError as exc:
        print(exc)

print(packages)

brew_installed = subprocess.run(["which", '"brew"'], capture_output=True)
print(brew_installed.stdout == b'')
if(brew_installed.stdout == b''):
    print("brew not installed, installing via script")
    install_brew = subprocess.run('NONINTERACTIVE=1 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"', shell=True)
    subprocess.run("export PATH=/home/linuxbrew/.linuxbrew/bin:$PATH", shell=True)

for package in packages:
    installed = subprocess.run(["which", package], capture_output=True)
    if(installed.stdout == b''):
        print(f"{package} missing, installing via brew")
        subprocess.run(["brew", "install", package])
    else:
        print(f"{package} already installed, skipping")

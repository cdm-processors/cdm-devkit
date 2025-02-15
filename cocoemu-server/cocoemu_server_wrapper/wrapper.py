#
# Python wrapper for cocoemu-server
#

from pathlib import Path
import shutil
import signal
import subprocess
import sys

JAVA_EXE = "java"
JAR_PATH = Path(__file__).parent / "jar" / "cocoemu-server.jar"


def main():
    if not JAR_PATH.exists():
        print(
            "Can't find cocoemu-server.jar. Try reinstalling package or contact developer."
        )
        exit(1)

    java_path = shutil.which(JAVA_EXE)

    if java_path is None:
        print(
            "Java is not found. Make sure you have Java 8 or newer installed and it is available in PATH"
        )
        exit(1)

    java_cmd = [java_path, "-jar", JAR_PATH.as_posix(), *sys.argv[1:]]
    print(" ".join(java_cmd))

    emulator_process = subprocess.Popen(java_cmd)

    try:
        emulator_process.wait()
    except KeyboardInterrupt:
        emulator_process.send_signal(signal.SIGINT)
        emulator_process.wait()
    except subprocess.CalledProcessError as e:
        sys.exit(e.returncode)


if __name__ == "__main__":
    main()

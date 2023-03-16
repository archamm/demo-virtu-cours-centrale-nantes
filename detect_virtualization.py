import platform

def detect_virtualization():
    system = platform.system()
    release = platform.release()
    version = platform.version()
    machine = platform.machine()
    processor = platform.processor()
    
    if "Linux" in platform.platform() or "vbox" in platform.platform().lower() or "xen" in platform.platform().lower() or "kvm" in platform.platform().lower():
        virtualization = "Yes"
    else:
        virtualization = "No"

    print(f"System: {system}")
    print(f"Release: {release}")
    print(f"Version: {version}")
    print(f"Machine: {machine}")
    print(f"Processor: {processor}")
    print(f"Is it running in a virtual environment? {virtualization}")

if __name__ == "__main__":
    detect_virtualization()

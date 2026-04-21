import numpy as np  # Numerical computing library
import random  # Random number generation (not currently used)

class CameraHandler:  # Camera management class
    def __init__(self):  # Constructor
        self.camera = None  # Camera object placeholder
        self.is_connected = False  # Connection status flag
        self.simulation_mode = False  # Simulation mode flag
        self.sdk = None  # Thorlabs SDK instance
        
        try:  # Try to initialize SDK
            from thorlabs_tsi_sdk.tl_camera import TLCameraSDK  # Import Thorlabs SDK
            self.sdk = TLCameraSDK()  # Create SDK instance
            print("Thorlabs camera SDK initialized successfully.")  # Success message
        except Exception as e:  # SDK initialization failed
            print(f"SDK not found or init failed ({e}). Switching to Simulation Mode.")  # Fallback message
            self.sdk = None  # Clear SDK reference
            self.simulation_mode = True  # Enable simulation mode

    def connect(self):  # Connect to camera
        if self.simulation_mode:  # Already in simulation mode
            print("Simulated Camera connected.")  # Status message
            self.is_connected = True  # Mark as connected
            return True  # Connection successful
            
        try:  # Try hardware connection
            devices = self.sdk.discover_available_cameras()  # Find available cameras
            if len(devices) > 0:  # If cameras found
                self.camera = self.sdk.open_camera(devices[0])  # Open first camera
                self.camera.arm(frames_to_buffer=10)  # Prepare camera for capture
                self.is_connected = True  # Mark as connected
                return True  # Connection successful
        except Exception as e:  # Connection attempt failed
            print(f"Camera connection failed ({e}). Using Simulation Mode.")  # Error message
        
        print("No Hardware found. Using Simulation Mode.")  # Fallback message
        self.simulation_mode = True  # Enable simulation mode
        self.is_connected = True  # Mark as connected (simulation)
        return True  # Return success

    def get_fringe_intensity(self):  # Get fringe intensity value
        if self.simulation_mode:  # Simulation mode active
            import time  # Time module for oscillation
            value = 200 if int(time.time() * 2) % 2 == 0 else 50  # Alternate between 200 and 50
            print("SIM INTENSITY:", value)  # Debug output
            return value  # Return simulated value
                
        # Real hardware logic
        if self.camera:  # Camera connected
            self.camera.issue_software_trigger()  # Trigger camera to capture frame
            for _ in range(10):  # Wait up to 10 attempts for frame
                frame = self.camera.get_pending_frame_or_null()  # Get latest frame
                if frame is not None:  # Frame available
                    img = frame.image_buffer  # Extract image data
                    h, w = img.shape  # Get image dimensions
                    return np.mean(img[h//2-10:h//2+10, w//2-10:w//2+10])  # Return center region average
                import time
                time.sleep(0.001)  # Short wait before retry
        return None  # No valid data
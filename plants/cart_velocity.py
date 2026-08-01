class CartVelocity:
    PARAMS = {
        "mass": {"prompt": "Mass", "type": float},
        "opposing_force": {"prompt": "Opposing Force (Drag/Friction)", "type": float},
        "v_initial": {"prompt": "Initial Velocity", "type": float, "default": 0.0},
    }

    def __init__(self, mass, opposing_force, v_initial=0.0):
        if mass <= 0:
            raise ValueError("mass must be positive.")
        self.m = mass
        self.b = opposing_force
        self.v_initial = v_initial
        self.v_current = self.v_initial

    def step(self, u, dt):
        v_new = self.v_current + ((u - (self.b * self.v_current)) / self.m) * dt
        self.v_current = v_new
        return self.v_current

    def get_state(self):
        return self.v_current

    def reset(self):
        self.v_current = self.v_initial
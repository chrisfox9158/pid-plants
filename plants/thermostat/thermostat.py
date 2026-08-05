class Thermostat:
    PARAMS = {
        "control_scale": {"prompt": "Control Scale (strength of thermostat effects)", "type": float, "default": 1.0},
        "response_scale": {"prompt": "Response Scale (high = slow-heating; low = fast-heating)", "type": float, "default": 60.0},
        "t_ambient": {"prompt": "Ambient (Room) Temperature", "type": float, "default": 21.0},
        "t_initial": {"prompt": "Initial Temperature", "type": float, "default": None},
    }
    
    def __init__(self, control_scale, response_scale, t_ambient=21.0, t_initial=None):
        if response_scale <= 0:
            raise ValueError("response_scale must be positive.")
        if t_initial is None:
            t_initial = t_ambient

        self.k = control_scale
        self.tau = response_scale
        self.t_ambient = t_ambient
        self.t_initial = t_initial
        self.t_current = self.t_initial

    def step(self, u, dt):
        t_new = self.t_current + ((-(self.t_current - self.t_ambient) + self.k * u) / self.tau) * dt
        self.t_current = t_new
        return self.t_current

    def get_state(self):
        return self.t_current

    def reset(self):
        self.t_current = self.t_initial
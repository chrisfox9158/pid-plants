from collections import deque
import math

class ThermostatDelayed:
    PARAMS = {
        "control_scale": {"prompt": "Control Scale (strength of thermostat effects)", "type": float, "default": 1.0},
        "response_scale": {"prompt": "Response Scale (high = slow-heating; low = fast-heating)", "type": float, "default": 60.0},
        "t_ambient": {"prompt": "Ambient (Room) Temperature", "type": float, "default": 21.0},
        "t_initial": {"prompt": "Initial Temperature", "type": float, "default": None},
        "dt": {"prompt": "Timestep (should match arg-passed timestep)", "type": float, "default": 1},
        "theta": {"prompt": "Dead Time (time before control affects system)", "type": float, "default": 5.0},
    }
    
    def __init__(self, control_scale=1.0, response_scale=60.0, t_ambient=21.0, t_initial=None, dt=1, theta=5.0):
        if response_scale <= 0:
            raise ValueError("response_scale must be positive.")
        if t_initial is None:
            t_initial = t_ambient

        self.k = control_scale
        self.tau = response_scale
        self.t_ambient = t_ambient
        self.t_initial = t_initial
        self.t_current = self.t_initial
        self.dt = dt
        self.theta = theta
        raw_maxlen = self.theta / self.dt
        self.maxlen = max(1, int(math.ceil(raw_maxlen)))
        self.u_values = deque(maxlen=self.maxlen)

    def step(self, u, dt):
        if dt != self.dt:
            raise RuntimeError("step() timestep does not equal plant class timestep; please ensure initial dt matches the passed step() dt value.")

        if len(self.u_values) >= self.maxlen:
            u_delayed = self.u_values[0]
        else:
            u_delayed = 0
        t_new = self.t_current + ((-(self.t_current - self.t_ambient) + self.k * u_delayed) / self.tau) * dt

        self.t_current = t_new
        self.u_values.append(u)
        return self.t_current

    def get_state(self):
        return self.t_current

    def reset(self):
        self.t_current = self.t_initial
        self.u_values = deque(maxlen=self.maxlen)
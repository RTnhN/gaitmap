from gaitmap.trajectory_reconstruction.trajectory_methods import (
    compiled_kalman_funcs,
)

try:
    compiled_kalman_funcs.cc.compile()
except AttributeError:
    print("The compiled Kalman funcs have already been compiled.")  # noqa: T201

from gaitmap.trajectory_reconstruction.trajectory_methods import (
    compiled_kalman_funcs,
)

compiled_kalman_funcs.cc.compile()

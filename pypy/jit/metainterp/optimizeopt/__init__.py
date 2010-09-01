from optimizer import Optimizer
from rewrite import Rewrite

def optimize_loop_1(metainterp_sd, loop, virtuals=True):
    """Optimize loop.operations to make it match the input of loop.specnodes
    and to remove internal overheadish operations.  Note that loop.specnodes
    must be applicable to the loop; you will probably get an AssertionError
    if not.
    """
    optimizations = (Rewrite(),)
    optimizer = Optimizer(metainterp_sd, loop, optimizations)
    if virtuals:
        optimizer.setup_virtuals_and_constants()
    optimizer.propagate_all_forward()

def optimize_bridge_1(metainterp_sd, bridge):
    """The same, but for a bridge.  The only difference is that we don't
    expect 'specnodes' on the bridge.
    """
    optimize_loop_1(metainterp_sd, bridge, False)
        

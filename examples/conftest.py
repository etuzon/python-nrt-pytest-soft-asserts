import pytest


@pytest.fixture(autouse=True)
def run_before_test(request):
    markers = request.node.own_markers

    for marker in markers:
        if marker.name == 'soft_asserts':
            marker_params = marker.kwargs
            soft_asserts = marker_params['soft_asserts']
            skip_steps = marker_params['skip_steps']

            for step in skip_steps:
                if soft_asserts.is_step_in_failure_steps(step):
                    pytest.skip(f'Skipped because [{step}] failed.')

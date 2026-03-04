import pytest

from codewars_kyus.kyu_1.job_matching_n1 import job_matching

candidate1 = {'min_salary': 120000}
candidate2 = {'min_salary': 190000}
job1 = {'max_salary': 130000}
job2 = {'max_salary': 80000}
job3 = {'max_salary': 171000}


@pytest.mark.parametrize(
    "candidate,job,output", [
        (candidate1, job1, False),
        (candidate1, job2, False),
        (candidate1, job3, True),
        (candidate2, job1, False),
        (candidate2, job2, False),
        (candidate2, job3, True),
    ]
)
def test_job_matching(candidate, job, output):
    assert job_matching(candidate, job) == output

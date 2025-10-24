class Solution:
    def job_scheduling(starts, ends, profits):
        jobs = sorted(zip(starts, ends, profits),
                      key=lambda x: x[1])
    
        dp = [0] * (len(jobs) + 1)
        for i in range(1, len(jobs) + 1):
            start, end, profit = jobs[i - 1]
            # find number of jobs to finish before start of current job
            num_jobs = bisect_right([job[1] for job in jobs], start)
            
            dp[i] = max(dp[i - 1], dp[num_jobs] + profit)
            
        return dp[-1]

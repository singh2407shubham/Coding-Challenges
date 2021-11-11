# moving average

nums = [1,6,5,8,4,9,6,2,4,3]
k = 3

def slidingWindowAverage(nums, k):
  cur_sum = 0
  res = []
  for i in range(len(nums)-k + 1):
    if i == 0:
      cur_sum = sum(nums[0:i+k])
    else:
      cur_sum -= nums[i-1]
      cur_sum += nums[i+k-1]
    res.append(round(cur_sum/k, 2))
  return res

ans = slidingWindowAverage(nums,k)
print(ans)

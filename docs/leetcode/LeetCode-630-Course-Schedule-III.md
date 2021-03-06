## 解题思路

如果在现实生活中，我们遇到题目中的选课问题，要求学完最多的课，该如何选择？
因为一门课程开始学习的日期是任意的，只要在课程截止日期修完即可。因此影响我们选课的因素只有两个：

- 课程的截止时间，越早截止的课程越要放在前面学完；
- 课程的学习时长，课时越短的课程越要放在前面学完；

那影响因素 1 和 2，哪个更优先处理？因为一旦过截止日，课程无法再学习。所以先对课程表按截止日期排序,依此学习课程。假设当前日期为 `n`，即将开始学习的课程为 `course[i] = [x, y]`：

- 如果 `n + x <= y`，表明 `courses[i]` 可以学完；
- 否则 `courses[i]` 在当前计划中无法学习完，要把之前学习过的课时最长的课程剔除掉；

由此可见，这里存在一个大根堆，即堆的顶点始终存储当前已经学习过的课时最长的课程。

## 参考代码

```python3
```

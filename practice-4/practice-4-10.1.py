#問題4-10: ロボット芸人
timer, executions = 6, 2
input_data = [[2,"foo"],[3,"bar"]]
set_timer_list = []
strings = []

for i in range(executions):
    set_timer, string = input_data[i]
    set_timer_list.append(int(set_timer))
    strings.append(string)

for time in range(1, timer + 1):
    result = " ".join(strings[index] for index, set_time in enumerate(set_timer_list) if time % set_time == 0)
    print(result if result else time)
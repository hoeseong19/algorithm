class Feature():
    def __init__(self, progress, speed):
        self.progress = progress
        self.speed = speed

    def process(self):
        self.progress += self.speed

    def is_finished(self):
        is_finished = self.progress >= 100

        return is_finished


def solution(progresses, speeds):
    answer = []

    feature_length = len(progresses)
    feature_list = []
    for i in range(feature_length):
        progress = progresses[i]
        speed = speeds[i]

        feature = Feature(progress, speed)
        feature_list.append(feature)

    # 작업은 순차적임
    # 끝나야 되는 작업의 순서를 인덱스로 저장
    finished_feature_count = 0

    while (finished_feature_count < feature_length):
        for feature in feature_list[finished_feature_count:]:
            if not feature.is_finished():
                feature.process()

        # 끝나는 날은 중요하지 않음
        # 작업이 끝나는 시점에 얼마나 많은 작업이 끝났는 지가 중요
        count = 0
        for feature in feature_list[finished_feature_count:]:
            if not feature.is_finished():
                break
            # 만약 하나라도 끝났으면
            # 완료된 다음 작업까지, 혹은 마지막까지 순회

            finished_feature_count += 1
            count += 1

        # 작업이 완료되지 않은 경우, 여태까지 완료된 작업의 수를 저장
        if count != 0:
            answer.append(count)

    return answer

print(solution([93, 30, 55],[1, 30, 5])==[2, 1])
print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])==[1, 3, 2])

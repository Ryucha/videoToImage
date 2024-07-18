import os
import subprocess

script_dir = os.path.dirname(os.path.abspath(__file__))

# 비디오 파일이 있는 디렉토리 경로 (상대 경로 사용)
input_directory = os.path.join(script_dir, 'videos')
# 이미지가 저장될 디렉토리 경로 (상대 경로 사용)
output_directory = os.path.join(script_dir, 'output_images')

# 출력 디렉토리가 없으면 생성
if not os.path.exists(output_directory):
    os.makedirs(output_directory)
    
# 모든 비디오 파일에 대해 이미지 추출
for filename in os.listdir(input_directory):
    if filename.endswith(".mp4"):
        # 입력 및 출력 파일 경로 설정
        input_path = os.path.join(input_directory, filename)
        output_filename = os.path.splitext(filename)[0] + '%04d.png'
        output_path = os.path.join(output_directory, output_filename)
        
        # FFmpeg 명령어 실행
        ffmpeg_command = [
            'ffmpeg', '-i', input_path, '-vf', 'fps=1', output_path
        ]
        
        print(f'Processing file: {input_path}')
        subprocess.run(ffmpeg_command)
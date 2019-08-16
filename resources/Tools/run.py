import os
import sys
from pathlib import Path

# print(Path.home(),Path.cwd())
# project= r"\footlbotestproj"
# print(str(Path.home())+project)

current_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 到suite 目录
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)


# proj_root = os.path.dirname(os.path.abspath(__file__))
# if proj_root not in sys.path:
#     sys.path.insert(0, proj_root)
# exlib_dir = os.path.join(proj_root, 'exlib')

path = root_path
print(path)
print(Path.cwd())
print(Path.home())
print(sys.path)
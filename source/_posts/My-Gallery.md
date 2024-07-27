---
layout: photo
title: My Gallery
date: 2024-07-27 15:00:08
cover: https://qiniu.sukoshi.xyz/src/images/68686407_p0.jpg
---
Welcome to [Hexo](https://hexo.io/)! This is your very first post. Check [documentation](https://hexo.io/docs/) for more info. If you get any problems when using Hexo, you can find the answer in [troubleshooting](https://hexo.io/docs/troubleshooting.html) or you can ask me on [GitHub](https://github.com/hexojs/hexo/issues).

```python
import os
import glob
import random

def get_random_image(directory):
    images = glob.glob(os.path.join(directory, "*.jpg"))
    return random.choice(images)

```
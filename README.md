# Actions

**All input options are of type string.**

## compile-latex-and-upload-pdf
An action to auto compiling LaTeX project and upload pdf files to latex2pdf release.

Required input option:
- latex_project_dir: [string]. For example: manuals or manuals/toggle_language
- cls_file_is_in_project_dir: [true or false]
- access_token: [your github token]. You could pass token with github action secrets.

## setup-latex-action
An action to setup LaTeX environment for doc class.

## install-fonts
An action to install fonts for LaTeX environment.

Required input option:
- font_name: [list]. For example:
    ```yaml
    font_name: |
    AlibabaPuHuiTi3.0
    shetumodengxiaofangti
    FreeHKKai4700
    pinrushouxieti
    ```

## Author
**Actions** © Mr. Kin, all files released under the [WTFPL][] license.

Authored and maintained by Mr. Kin.

> [Blog][] · [GitHub][] · [Weibo][] · [Zhihu][] · [AcFun][] · [Bilibili][] · [Youku][] · [Headline][] · [YouTube][]

[WTFPL]: ./LICENSE
[Blog]: https://mister-kin.github.io
[GitHub]: https://github.com/mister-kin
[Weibo]: https://weibo.com/6270111192
[Bilibili]: http://space.bilibili.com/17025250?
[Youku]: http://i.youku.com/i/UNjA3MTk5Mjgw?spm=a2hzp.8253869.0.0
[YouTube]: https://www.youtube.com/@Mister-Kin
[Headline]: https://www.toutiao.com/c/user/835254071079053/#mid=1663279303982091
[Zhihu]: https://www.zhihu.com/people/drwu-94
[AcFun]: https://www.acfun.cn/u/73269306

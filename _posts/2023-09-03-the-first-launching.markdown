---
layout: post
title: "The First Launching"
date: 2023-09-03 20:00:00 +0700
categories: meta
tags: updates
---

<figure class="post-banner">
  <img src="{{site.url}}/assets/img/posts/2023-09-03-the-first-launching.png" alt="The First Launching"/>
  <figcaption>This website at the time of its first launch</figcaption>
</figure>

3, 2, 1, liftoff!

I've been wanting to have a personal website for a long time, but I never got the chance to do it. Until now! If you check the GitHub repository of this website, you'll find out that I've been working on it since years ago. 

In this website, I plan to write about programming related topics, mostly about maintainability, testability, reusability, functional programming, and React. Sometimes, I will also write things about games and One Piece. Don't worry, they will be on different categories so it won't be mixed up with the programming stuffs. As you may have noticed, this website is written using Jekyll. It's a pretty _unique_ static site generator. It takes quite some times to get used to it especially when you're used to the luxury of modern web frameworks such as React and Vue. Still worth it though!

As you can see right now, this website is still very barebone. It does not even work on phones yet! Also, I also have a lot features in mind that I want to add to this website. But I think it's better to launch it now and add the features later. You know, make it happen first and make it better later. My priorities in the near future would be:

* Responsivity
* Several programming posts
* Optimizations
* Portfolio
* Visual features
* More posts!

I also want to showcase how `codes` will look in this website. Here's a sample of not-super-optmized-black-magic TypeScript code that transforms a snake-case object type into a camel-case object type:
  
{% highlight typescript %}
type SnakeToCamelCase<T extends string> = 
  T extends `${infer A extends string}_${infer B extends string}` 
    ? `${A}${Capitalize<SnakeToCamelCase<B>>}` 
    : T

type NormalizeField<T> = {
    [Key in keyof T as SnakeToCamelCase<Exclude<Key, number | symbol>>]: 
        T[Key] extends Record<string, unknown> 
            ? NormalizeField<T[Key]>
            : T[Key] extends Array<infer I>
            ? I extends Record<string, unknown>
            ? Array<NormalizeField<I>>
            : Array<I>
            : T[Key]  
{% endhighlight %}

That's it for now. I hope you enjoy reading this. Let's look forward to what comes next! Adios~

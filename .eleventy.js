const yaml = require("js-yaml");

module.exports = function(eleventyConfig) {
  eleventyConfig.addPassthroughCopy('assets');
  eleventyConfig.addDataExtension("yml,yaml", contents => yaml.load(contents));

  eleventyConfig.addFilter("findByKey", (list, key) => {
    return list?.find(item => item.key === key);
  });


  return {
    dir: {
      input: "content",
      output: "dist",
      data: "../data",
      includes: "../site/_includes",
      layouts: "../site/_layouts",
    },
  };
};

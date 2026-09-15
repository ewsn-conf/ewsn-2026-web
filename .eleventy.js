const yaml = require("js-yaml");

module.exports = function(eleventyConfig) {
  eleventyConfig.addPassthroughCopy('assets');
  eleventyConfig.addDataExtension("yml,yaml", contents => yaml.load(contents));

  return {
    dir: {
      input: "content",
      output: "dist",
      data: "../site/_data",
      includes: "../site/_includes",
      layouts: "../site/_layouts",
    },
  };
};

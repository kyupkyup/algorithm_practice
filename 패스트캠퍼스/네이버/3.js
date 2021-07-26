const fetchApi = async () => {
  const url = 'http://example.com/articles';
  try {
    const result = await fetch(url);
    return result.json();
  } catch (e) {
    console.error(e);
  }
  //   if(!result) throw new Error('no result')
  //   .then(res => res.json())
  //   .catch(rej => console.error(rej));
};

const renderArticle = (title, content) => {
  const $container = document.createElement('div');
  const $articleTitle = document.createElement('div');
  const $articleContent = document.createElement('div');
  $container.setAttribute('class', 'article');
  $articleTitle.setAttribute('class', 'article-title');
  $articleContent.setAttribute('class', 'article-content');
  $articleTitle.textContent = title;
  $articleContent.textContent = content;
  $container.appendChild($articleTitle);
  $container.appendChild($articleContent);
  return $container;
};

const render = articles => {
  const $list = document.querySelector('.articles-list');
  articles.map(({ title, content }) => $list.appendChild(renderArticle(title, content)));
};

const solution = async () => {
  const result = await fetchApi();
  render(result);
};
